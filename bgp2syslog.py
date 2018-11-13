#!/usr/bin/env python

# adapted from https://github.com/Exa-Networks/exabgp/blob/master/etc/exabgp/run/syslog-1.py

import os
import sys
import syslog

syslog.openlog("%s[%d]" % ("ExaBGP",os.getpid()))

# When the parent dies we are seeing continual newlines, so we only access so many before stopping
counter = 0

while True:
	try:
		line = sys.stdin.readline().strip()
		if line == "":
			counter += 1
			if counter > 100:
				break
			continue

		counter = 0

		syslog.syslog(syslog.LOG_ALERT, line)
	except KeyboardInterrupt:
		pass
	except IOError:
		# most likely a signal during readline
		pass
