#!user/bin/python
# -*- coding: utf-8 -*-
import urllib2, base64
import requests
import json
import unicodedata
from tokensTeamWork import *
from teamworkcreateatask import *
from urllib2 import urlopen,base64
import sys
import time
from datetime import datetime, timedelta
reload(sys)

#here get all lista user
def getAllUser():
    status = 0
    r = requests.get(url + '/companies/98191/people.json', auth=(key,''))
    data = json.loads(r.text, encoding='utf-8', cls=None, object_hook=None, parse_float=None, parse_int=None,parse_constant=None, object_pairs_hook=None)
    return data

#here get a list of all day lab.
def getDays(startDate,endDate):
    laborabledays = []
    k = 0
    #Here created  a range of days
    splitStartDate = str(startDate).split("-")
    splitEndDate = str(endDate).split("-")

    startdate = datetime(int(splitStartDate[0]), int(splitStartDate[1]), int(splitStartDate[2]))
    enddate = datetime(int(splitEndDate[0]), int(splitEndDate[1]), int(splitEndDate[2]))

    list_dates = [(startdate + timedelta(days=d)).strftime("%Y-%m-%d") for d in range((enddate - startdate).days + 1)]
    for Daysvalues in list_dates:
        partday = str(Daysvalues).split("-")
        day = datetime(int(partday[0]), int(partday[1]), int(partday[2]))
        dayweeked = day.strftime('%A').upper()
        if dayweeked == 'SUNDAY' or dayweeked == 'SATURDAY':
            pass
        else:
            laborabledays.insert(k, str(Daysvalues))
    return laborabledays

def getDaysLastWeek():
    # Set Monday Today print time.strftime('%d %m %y')
    Year = int(time.strftime('%Y'))
    Mount = int(time.strftime('%m'))
    Day = int(time.strftime('%d'))
    mondayDay = datetime(Year, Mount, Day)
    fridaySet = mondayDay + timedelta(days=-3)
    friday = fridaySet
    monday = fridaySet + timedelta(days=-4)

    print ('Inicio : ' + str(monday.strftime("%Y-%m-%d")) + ' ---- ' + 'Final :' + str(friday.strftime("%Y-%m-%d")))
    startdate = monday
    enddate = friday

    list_dates = [(startdate + timedelta(days=d)).strftime("%Y-%m-%d") for d in range((enddate - startdate).days + 1)]
    return (list_dates)

def verifyConnectedTime():
    #Here get a list of all users
    listuser = getAllUser()
    #Here get a list of the days here send  today  day
    listdays = getDaysLastWeek()
    #Here count and set day to verify
    count_day = len(listdays)
    count_days_user = 0
    #Count of taskcreate
    count_task = 0
    #here ask if there are day in the teamwork without fill
    for dataUser in listuser['people']:

        # Here count  numbers'  days resgtred for the user
        for day in listdays:
            d1 = day.replace('-', '')
            r = requests.get(url + '/time.json?userId=' + str(dataUser['id']) + '&fromDate=' + str(d1), auth=(key, ''))
            data = json.loads(r.text, encoding='utf-8', cls=None, object_hook=None, parse_float=None, parse_int=None,
                              parse_constant=None, object_pairs_hook=None)
            registerDays = len(data['time-entries'])
            if registerDays > 0:
                count_days_user += 1

        if count_days_user == count_day:
            count_days_user = 0
        else:
            print('ID:' + str(dataUser['id']) + ' Name:' + str(dataUser['first-name'] + ' ' + str(dataUser['last-name'])))
            listUsers = '216004,215992'
            listUsers += ',' + str(dataUser['id'])
            listGrantAcces = '216004,215992'
            listGrantAcces += ',' + str(dataUser['id'])
            count_task += 1
            print('Cear Tareas de registro')
            print('Dias registrado ' + str(count_days_user) + '/5')
            print(str(count_task) + '.-' + 'dayStart=' + str(listdays[0]) +  ',dayEnd=' + str(listdays[4]) + ',listUser=' + str(listUsers) +  ',listGrantAcces=' + str(listGrantAcces))
            create_a_task(dayStart=listdays[0], dayEnd=listdays[4], listUser=listUsers, listGrantAcces=listGrantAcces)
            count_days_user = 0


    print ('---------------------------------------------------------------------')
    print ('Total create task :' + str(count_task))
#############################################################################################
##                                                                                         ##
##                                                                                         ##
##                                  main function                                          ##
##                                                                                         ##
#############################################################################################



