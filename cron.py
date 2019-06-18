import os
import logging

from crontab import CronTab

# import socketio
from socketIO_client import SocketIO, LoggingNamespace

import requests


# On définit le  client socket
# sio = socketio.Client()
socketIO = SocketIO('localhost', 3000, LoggingNamespace)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

API_ENDPOINT = "http://localhost:3000/api/insert"

# @sio.on('connect')
# def connect():
#     print('connection established')


# @sio.on('discconnect')
# def disconnect():
#     print('disconnected from server')


# @sio.on('ready')
# def ready(sid, data):
def ready(*args):
    print('ready')
    # Broadcast event
    # if data['unit'] == unit:
    # Si l'unité cible est bien celle actuelle, alors on envoie le contenu du fichier json au serveur
    myFile = open('data.json', 'r')
    # sio.emit('send-data', {'data': myFile.read()})
    data = myFile.read()
    print(data)
    # socketIO.emit('send-data', {'data': data})

    # Si le socket n'est pas fonctionnel, on utilise la fonction API mise en place à cete effet
    response = requests.post(url=API_ENDPOINT, data={"data": data})
    print(response.text)

    myFile.close()


# @sio.on('file-ready')
def file_ready(unit):
    # sio.sleep(10)
    # socketIO.connect()
    socketIO.wait(seconds=10)
    # sio.emit('file-ready', {'unit': unit})
    socketIO.emit('file-ready', {'unit': unit})


# sio.connect('localhost:5000')
# sio.wait()

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
 # job.every_reboot()

# on enregistre la tâche plannifiée et on démarre le job
cron.write()

# file_ready(unit)

if job.is_valid()==True:
    job_standard_output = job.run()
    print(job_standard_output)

# on envoie un event au serveur après 10 sec pour signifier que le fichier est prèt à être récupéré
# ready()

file_ready(unit)
socketIO.on('ready', ready)
