#!user/bin/python
# -*- coding: utf-8 -*-

#imports for jso and request
from tokensTeamWork import *
from urllib2 import urlopen,base64
import json
import requests
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
from datetime import datetime, timedelta

#Here the url
#/tasks/{id}.json
#{
#  "todo-item": {
#    "content": "Test Task",
#    "notify": false,
#    "description": "Test Task Sub Item",
#    "due-date": "20140405",
#    "start-date": "20140402",
#    "estimated-minutes": "0",
#    "private": 0,
#    "grant-access-to": "",
#    "priority": "low",
#    "progress": "20",
#    "attachments": [],
#    "pendingFileAttachments": "",
#    "responsible-party-id": 0,
#    "predecessors": [
#      {
#        "id": 439492,
#        "type": "complete"
#      }
#    ],
#    "tags": "api,documentation",
#    "commentFollowerIds": "",
#    "changeFollowerIds": "",
#    "positionAfterTask": -1
#  }
#}


def create_a_task(dayStart,dayEnd,listUser,listGrantAcces,idUser):

    Year = int(time.strftime('%Y'))
    Mount = int(time.strftime('%m'))
    Day = int(time.strftime('%d'))
    Day1 = datetime(Year, Mount, Day)

    #Here set first day for starDaue
    StarDateDue = Day1.strftime("%Y%m%d")

    #Here set final date for EndDateDue
    FinalDate = Day1 + timedelta(days=4)
    EndDateDue = FinalDate.strftime("%Y%m%d")

    message = 'Hola revisando las actividades de tus proyectos , he notado que te faltan dias por registrar.\n'
    message += 'Para poder arreglar este problema accede a está url.\n'
    message += 'https://forta.teamwork.com/#people/' +  str(idUser)  + '/time\n'
    #data[''] =
    data = {'todo-item': {}}
    data['todo-item']['content'] = 'Hay un problema con tú registro de actividades periodo ' + str(dayStart) + ' al '  +  str(dayEnd)
    data['todo-item']['responsible-party-id'] = listUser
    data['todo-item']['notify'] = 'true'
    data['todo-item']['description'] = str(message)
    data['todo-item']['due-date'] = str(EndDateDue)
    data['todo-item']['start-date'] = str(StarDateDue)
    data['todo-item']['grant-access-to'] = listGrantAcces
    data['todo-item']['priority'] = 'high'
    dataJson = json.dumps(data)
    r = requests.post( url  + '/tasklists/1671606/tasks.json', auth=(keyBot, ''), data=dataJson)
    return r.text