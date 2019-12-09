import getpass
import sys
from telnetlib import Telnet

host = "127.0.0.1"
port = 910
timeout=10
def getNum():
	with open("num-list.txt","r") as f:
		num=f.readline().strip()
		print ("Trying the number now" , str(num))
		putNum(num)
def putNum(num):
	s=Telnet(host,port,timeout)
	print ("connection established")
	print (s.write(str(num)+"\n"))
	print (s.read_all())
	#s.expect("[!] Access denied, disconnecting client....")
getNum()
