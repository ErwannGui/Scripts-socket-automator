import os

from crontab import CronTab

import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web

import socketio

unit = 1

define("port", default=3000, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

sio = socketio.AsyncServer(async_mode='tornado')

@sio.on('reaedy', namespace='/test')
async def send_data(sid, data):
    # Broadcast event
    if data['unit'] == unit:
        myFile = open('data.json', 'r')
        await sio.emit('send-data', {'data': myFile.read()}, namespace='/test')
        myFile.close()

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/socket.io/", socketio.get_tornado_handler(sio)),
        ],
        debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    cron_task()


async def cron_task():
    # cron = CronTab()
    cron = CronTab(user='admwiart')
    # cron = CronTab(tabfile='task.tab')
    # cron = CronTab(tab="""
    #   * * * * * command
    # """)
    job = cron.new(command='python script.py')
    job.minute.every(1)
    job.every_reboot()

    cron.write()

    await sio.sleep(10)
    await sio.emit('file-ready', {'unit': 1},
             namespace='/test')

    print(job.is_valid())

if __name__ == '__main__':
    main()