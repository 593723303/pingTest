#!/usr/bin/python
from __future__ import print_function
import subprocess
import threading
import re
from Queue import Queue
from Queue import Empty


isReacheable = []
unReacheable = []

def call_ping(ip):
	if subprocess.call(['ping', '-c', '1', ip]):
	#	print('{0} is active'.format(ip))
		isReacheable.append(ip)
	else:
	#	print('{0} is unreachable'.format(ip))
		unReacheable.append(ip)

def is_reachable(q):
	try:
		while True:
			ip = q.get_nowait()
			call_ping(ip)
	except Empty:
		pass


def main():
	q = Queue()
	Threach = [];
	with open('ip.txt') as f:
		lines = f.readlines()
		for line in lines:
			q.put(re.sub('\\n','',line))

	for i in range(10):
		thr = threading.Thread(target=is_reachable, args=(q,))
		thr.start()
		Threach.append(thr)
	for thr in Threach:
		thr.join()
	print('is reacheable ip:',isReacheable)
	print('un reacheable ip:',unReacheable)

if __name__ == '__main__':
	main()







