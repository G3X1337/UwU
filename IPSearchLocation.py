# IP Tracker
# Coded by Al GQ Infection
#Copyright InfectSec
#Hacking, Securing and Developing

import os

def oi():
	print("*******************************************************")
	print("Infection Security")
	print("Hacking, Securing and Developing")
	print("Coded by Al GQ Infection")
	print("IP Tracker")
	print("*******************************************************")
oi()
pilihan = input("}=> ENTER!!!")

from urllib.request import urlopen
import json

def mainProgram():
	while True:
		ip = input("\nInput IP to search: ")
		url = "http://ip-api.com/json/"
		response = urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("\nIP: " + values['query'])
		print("\nCountry: " + values['country'])
		print("\nRegion: " + values['regionName'])
		print("\nCity: " + values['city'])
		print("\nPostCode: " + values['zip'])
		print("\nISP: " + values['isp'])
		print("\nISP Name: " + values['org'])
		print("\nIP Owner: " + values['as'])
		break

mainProgram()
input('Press ENTER to exit!!!')
