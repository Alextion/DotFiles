#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################
#File Name:getNetTime.py
#Author:Alextion Jiang
#E-mail:alextion@gmail.com
#Creat Time:2017-05-03 14:37:49
########################################

import http.client
import time, os

def getNetTime(Url):
    conn = http.client.HTTPConnection(Url)
    conn.request("GET","/")
    r = conn.getresponse()
    # r.getheaders() get All http headers
    httpDate = r.getheader('date')
    # print(httpDate[5:25])
    ptime = time.strptime(httpDate[5:25], '%d %b %Y %H:%M:%S')
    # print(ptime)
    localtime = time.localtime(time.mktime(ptime)+8*60*60)
    # print(localtime)
    ftime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
    print("The Network TIme is %s." %ftime)
    cmds = "date --set='" + ftime + "'"
    print(cmds)
    try:
        os.system(cmds)
    except:
        print("WARRING:SET NETWORK TIME IS UNSUCESSFUL.")
    finally:
        print("Set Network Time Sucessful.")
if __name__ == '__main__':
    getNetTime('www.baidu.com')
