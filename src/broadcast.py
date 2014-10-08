#!/usr/bin/python


import argparse, sys, os, csv
from Yowsup.Common.utilities import Utilities
from Yowsup.Common.debugger import Debugger
from Yowsup.Common.constants import Constants
from Examples.EchoClient import WhatsappEchoClient
from Yowsup.Registration.v2.existsrequest import WAExistsRequest as WAExistsRequestV2
from Yowsup.Registration.v2.coderequest import WACodeRequest as WACodeRequestV2
from Yowsup.Registration.v2.regrequest import WARegRequest as WARegRequestV2
from Yowsup.Contacts.contacts import WAContactsSyncRequest

import threading,time, base64
import time
import MySQLdb as mdb
import sys
#CONSTANTS
pathdb = '/root/Desktop/project/Record.db' #DB Path Changes on the main machine
from Yowsup.connectionmanager import YowsupConnectionManager

DEFAULT_CONFIG = os.path.expanduser("~")+"/.yowsup/auth"
COUNTRIES_CSV = "countries.csv"



def startDbusInterface():
	from dbus.mainloop.glib import DBusGMainLoop
	from Yowsup.Interfaces.DBus.DBusInterface import DBusInitInterface
	import gobject

	DBusGMainLoop(set_as_default=True)

	DBusInitInterface()

	mainloop = gobject.MainLoop()

	gobject.threads_init()
	print("starting")
	mainloop.run()


def resultToString(result):
	unistr = str if sys.version_info >= (3, 0) else unicode
	out = []
	for k, v in result.items():
		if v is None:
			continue
		out.append("%s: %s" %(k, v.encode("utf-8") if type(v) is unistr else v))

	return "\n".join(out)

if 1:
    	countryCode ="91"
	login ="919495895404"
	identity ="00:EB:2D:69:82:6A"
	password ="kHtx9jIo2/d9LnGkAswLN+UylOM="

	identity = Utilities.processIdentity(identity)
	password = base64.b64decode(bytes(password.encode('utf-8')))
	Debugger.enabled = False
	#phones = ['918281867134@s.whatsapp.net']
	count = -1
#db input must be sent here
	con = mdb.connect('localhost', 'root', 'toor', 'radio');
	s=[]
	with con:

		cur = con.cursor()
		cur.execute("SELECT JID FROM Registration WHERE Channel=0")
    		while True:
			row = cur.fetchone()
                        count +=1

        		if row == None:
       				break
			s.append(row[0])
        print "channel active"
        message = raw_input("Enter your message :")
	message = message.replace("spacer","\n")
#now s has all the required values .
        t = count/250
	i = -250
        j = 0
	num = 0
	phones = []
	while(num < t):
		i += 250
		j +=250
	  	while(i<j):
         		phones.append(s[i])
			i+=1

	     	wa = WhatsappEchoClient(phones, message, True)
		wa.login(login, password)
        	num+=1
		phones = []
	i=j

        j= j+count%250
        # print j
	phones= []

   	while(i<j):
      	  	phones.append(s[i])
	        i+=1
    #print phones
	wa = WhatsappEchoClient(phones, message, True)
	wa.login(login, password)
