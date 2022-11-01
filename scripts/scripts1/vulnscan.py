#!/bin/python3

import socket
from IPy import IP
import pyfiglet
import subprocess
import time

#//clear the terminal window//
subprocess.call('clear', shell=True)

#//Port Scanner banner//
Port_Scanner_Banner = pyfiglet.figlet_format("Port Scanner")
print(Port_Scanner_Banner)

#//wait one second before procceding//
time.sleep(1)

#list to store open ports
ports =[]
#list to store discovered banners
banners =[]

def scan(target):
	'''//Scan target funtion//'''
	converted_ip = convert_ip(target)
	print('\n' + 'Scanning Target : ' + str(target))
	for port in range(21,80):
		scan_port(converted_ip, port)

def convert_ip(ip):
	'''//Funtion Converts the hostname if not already IP//'''
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

#def get_banner(s):
#	'''//function grabs and port banner and returns the data recieved//'''
#	return s.recv(1024)

def scan_port(ipaddress, port):
	'''///funtion scans Ports of the target and set the connection timeout///'''
	try:
		sock = socket.socket()
		sock.settimeout(.01)
		sock.connect((ipaddress, port))
		try:
			ports.append(port)
			banner = sock.recv(1024).decode().strip('\n').strip('\r')
			banners.append(banner)
		
		except:
			banners.append(' ')
			sock.close()
	except:
		pass
if __name__ == "__main__":
	targets = input( '[+] Enter Target/s To Scan(for multiple targets use a coma): ' )
	if ',' in targets:
		for ip_address in targets.split(','):
			scan(ip_address.strip(' '))
	else:
		scan(targets)




with open("vulnerable_banners.txt",'r') as file:
	count = 0
	for banner in banners:
		file.seek(0)
		for line in file.readline() :
			if line.strip() in banner:
				print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(ports[count]))
	count += 1

