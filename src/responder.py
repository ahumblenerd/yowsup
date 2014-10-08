#!/usr/bin/python


import argparse, sys, os, csv
from Yowsup.Common.utilities import Utilities
from Yowsup.Common.debugger import Debugger
from Yowsup.Common.constants import Constants
from Examples.ResponderClient import WhatsappResponderClient
from Yowsup.Registration.v2.existsrequest import WAExistsRequest as WAExistsRequestV2
from Yowsup.Registration.v2.coderequest import WACodeRequest as WACodeRequestV2
from Yowsup.Registration.v2.regrequest import WARegRequest as WARegRequestV2
from Yowsup.Contacts.contacts import WAContactsSyncRequest

import threading,time, base64

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
  cc=91
  phone=919495895404
  id=00:EB:2D:69:82:6A
  password=kHtx9jIo2/d9LnGkAswLN+UylOM=
	identity = Utilities.processIdentity(identity)
	password = base64.b64decode(bytes(password.encode('utf-8')))
	Debugger.enabled = False
#db input must be sent here
#	phones ='919746733813,91821455203,918281867134,919497366028,918943258740,918547126272'
#	message = raw_input("Enter your message :")
#	print ("number is %s" %phones)
#	print ("message is %s" %message)
	wa = WhatsappResponderClient(True, True)
	wa.login(login, password)
