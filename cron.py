import os

from crontab import CronTab

import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web

import socketio

unit = 1

# On définit les options de démarrage du client socket
define("port", default=3000, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

# et on initialise ce client
sio = socketio.AsyncServer(async_mode='tornado')


@sio.on('reaedy', namespace='/test')
async def send_data(sid, data):
    # Broadcast event
    if data['unit'] == unit:
        # Si l'unité cible est bien celle actuelle, alors on envoie le contenu du fichier json au serveur
        myFile = open('data.json', 'r')
        await sio.emit('send-data', {'data': myFile.read()}, namespace='/test')
        myFile.close()


async def cron_task():
    # On initialise la méthode d'utilisation de crontab
    # cron = CronTab()
    cron = CronTab(user='admwiart')
    # cron = CronTab(tabfile='task.tab')
    # cron = CronTab(tab="""
    #   * * * * * command
    # """)
    # et on créé une nouvelle tâche qui s'exécute à chaque reboot, toutes les minutes
    job = cron.new(command='python script.py')
    job.minute.every(1)
    job.every_reboot()

    # on enregistre la tâche plannifiée
    cron.write()

    # on envoie un event au serveur après 10 sec pour signifier que le fichier est prèt à être récupéré
    await sio.sleep(10)
    await sio.emit('file-ready', {'unit': unit},
             namespace='/test')

    print(job.is_valid())


def main():
    # on initialise notre client tornado socket avec les options définies plus haut
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/socket.io/", socketio.get_tornado_handler(sio)),
        ],
        debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    # après lancement du client, on démmare la tâche crontab
    cron_task()


if __name__ == '__main__':
    main()