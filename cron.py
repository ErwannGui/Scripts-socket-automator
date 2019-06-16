import os

from crontab import CronTab

import socketio

# On définit le  client socket
sio = socketio.Client()

@sio.on('connect')
def connect():
    print('connection established')


@sio.on('discconnect')
def disconnect():
    print('disconnected from server')


@sio.on('ready')
def ready(sid, data):
    # Broadcast event
    if data['unit'] == unit:
        # Si l'unité cible est bien celle actuelle, alors on envoie le contenu du fichier json au serveur
        myFile = open('data.json', 'r')
        sio.emit('send-data', {'data': myFile.read()})
        myFile.close()


@sio.on('file-ready')
def file_ready(unit):
    sio.sleep(10)
    sio.emit('file-ready', {'unit': unit})


sio.connect('localhost:5000')
sio.wait()

unit = 1

# On initialise la méthode d'utilisation de crontab
# cron = CronTab()
# cron = CronTab(user=True)
# cron = CronTab(user='admwiart')
cron = CronTab(tabfile='task.tab')
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
file_ready(unit)

print(job.is_valid())

