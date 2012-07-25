#!<<PYTHON>>
import time
import signal

def sighup(*args, **kwargs):
	print "Got HUP signal"
	exit()
signal.signal(signal.SIGHUP, sighup)

while 1:
	time.sleep(1.0)


