## -*- coding: utf-8 -*-
import socket
import time
import sys
import re
import random

import requests
from django.utils.encoding import smart_str, smart_unicode
from bs4 import BeautifulSoup


botnick = "Garbagtron" #Bot" + str(random.randint(1,999))
#botnick = "Encke"
#FREENODE
#channel = "#cafeMEMEMEADasda"
server = "irc.freenode.net"
#server = "irc.freenode.net"
# STYX irc
#channel = "#botnick"
port = 6667
count = 0


#users said list
listhow = ["hru", 'how are doing', 'how are you doing', 'what\'s up', 'how are you', 'How are things','Hiya', 'you?', 'whats goin on']
listGreets = ['hi', 'hey', 'hello', 'sup', 'yo', 'Howdy']
liststuff = ['666','licks','hugs','gives','<3',':)', 'makes']
#response
listhello = ['III', 'Nice to see you', 'Whazzup']
liststtuf = ['YAY!!', '404 error', 'Awww']
listfels = ['fine','ok', 'meh','awesome', 'everything black','heading towards the light']
listwelc = ['wb', 'Welcome', 'hey nice to see', 'happy to have you back', 'ACTION slaps ', 'whats up', 'WOW! You came back!', 'Welcome', 'appears']
listbyes = ['cya', 'see ya', 'bye', 'nice seeing you', 'have fun', 'dont die', 'Bye!! ', 'Bye']
#af_inet6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("\nConnecting to:" + server)
s.connect((server, port))
s.setblocking(False)
time.sleep(1)
p = s.recv(1048)
print(p)
time.sleep(1)
s.send("USER " + botnick + " " + botnick + " " + botnick + " :Bot WOW!\r\n")
time.sleep(1)
s.send("NICK " + botnick + "\n")
time.sleep(1)
s.send("JOIN " + channel + "\n")

while 1:
	time.sleep(0.1)
	try:
 		p = s.recv(1048)
		#print(p)
		print(p.lower())
	except Exception:
		pass

	if count == 30:
		user_name = p.split("!")[0]
		user_name = user_name.replace(":", "")

		if len(user_name) < 15 and ' ' not in user_name:
			user_name = user_name
		else:
			user_name == ""

		if p.find("PING") != -1:
			s.send("PONG "+ p.split()[1] + "\r\n")
		#if p.lower().startswith(':'+botnick.lower()):
		#	pass
		#else:
		#	if p.lower().find(channel)!=-1:
		#		for i in range(len(listGreets)):
		#			if p.lower().find(listGreets[i].lower())!=1:
		#				if p.lower().find(botnick.lower())!=-1:
		#					s.send("PRIVMSG "+channel+" :"+random.choice(listhello)+ " "+user_name +"\r\n")
		#		for i in range(len(listhow)):
		#			if p.lower().find(listhow[i].lower())!=-1:
		#				if p.lower().find(botnick.lower()) != -1:
		#					s.send("PRIVMSG "+channel+" :"+random.choice(listfels)+" "+user_name +"\r\n")
		#		for i in range(len(liststuff)):
		#			if p.lower().find(liststuff[i].lower()) != -1:
		#				if p.lower().find(botnick.lower()) != -1:
		#					s.send("PRIVMSG "+channel+" :"+random.choice(liststtuf)+" "+user_name+"\r\n")
		#		if p.lower().find(" join ") !=-1:
		#			if p.lower().find(" privmsg ")== -1:
		#				s.send("PRIVMSG "+channel+" :"+random.choice(listwelc)+ " "+user_name+"\r\n")
		#		if p.lower().find("quit") != -1 or p.lower().find("part") != -1:
		#			if p.lower().find(" privmsg ")== -1:
		#				s.send("PRIVMSG "+channel+" :"+random.choice(listbyes)+" "+user_name+" \r\n")#
		#if p.lower().find("!quit ")!=-1:
		#	quit()
					#lol
		if p.lower().find(channel.lower())!=-1:
			if p.lower().find("!weather")!=-1:
				if p.lower().find(" privmsg ")!= -1:
					place = p.split('!weather')
					if place[1] == '':
						pass
					try:
						location = "".join(place[1])
						url = "http://wttr.in/"+location.replace(' ','')+"?format=v2?lang=en"
						r  = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})
						html = r.content
						soup = BeautifulSoup(html,features="lxml")

						splited = soup.text.split('\n')
						splited = filter(None, splited)
						splited[0] = splited[0].replace('\r','')
						report = "".join(splited[0])
						report += " "
						report += "".join(splited[1])
						#report = report.encode('ascii','ignore')
						s.send("PRIVMSG "+channel+" :"+smart_str(report)+" also fuck you "+str(user_name)+"\r\n")
					except:
							#s.send("PRIVMSG "+channel+" : Error DipShit Detected ")
							pass
			if p.lower().find("!insult")!=-1:
				if p.lower().find(" privmsg ")!= -1:
					user = p.split('!insult')
					user = "".join(user[1])
					url = "http://www.robietherobot.com/insult-generator.htm"
					r  = requests.get(url)
					html = r.content
					soup = BeautifulSoup(html,'html.parser')
					test = soup.find_all('h1')
					test = "".join(test[1])
					test = test.replace('\t','').replace('\n','')
					test = test.encode('ascii','ignore')
					s.send("PRIVMSG "+channel+" :"+test+" "+str(user)+" also fuck you "+str(user_name)+"\r\n")

			if p.lower().find("http")!=-1:
				if p.lower().find(" privmsg ")!= -1:
					url = re.findall('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', p)
						#url = ''.join(url)
					for a_url in url:
						url = ''.join(a_url)
						html= requests.get(url, timeout=10)
						soup = BeautifulSoup(html.content, 'html.parser')
						url = soup.find('title', text=True)
						if url == None:
		        				pass
						else:
							if "Not Acceptable!" in url:
								pass
							url = url.get_text()
							url = url.replace('\n', ' ').replace('\r',' ')
							s.send("PRIVMSG "+channel+" :"+smart_str(url)+"\r\n")


	else:
		count+=1
	p=""
