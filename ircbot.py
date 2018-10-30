#!/usr/bin/python3
import socket, string


server = input("What server would you like to join?")

irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
irc.connect((server,6667))

user = "Anthony.Littlefield".encode('utf-8')
real = "Anthony Littlefield".encode('utf-8')
channel = "#cmsc491"

irc.send("USER ".encode('utf-8') + user + " ".encode('utf-8') + user + " ".encode('utf-8') + real + ":Active Cyber Defense  \n".encode('utf-8'))
irc.send("NICK er88255 \n".encode('utf-8'))
irc.send("JOIN ".encode("utf-8") + channel.encode("utf-8") + " \n".encode('utf-8'))

while(1):
	received = irc.recv(1024)
	print(received)
	decoded = received.decode('utf-8')
	com = decoded.split(" ")
	if com[0] == "PING":
    		print("you've gotten pinged!")
    		irc.send("PONG %s".encode('utf-8') % com[1].encode('utf-8') + "\n".encode('utf-8'))
	if received.find(b"!IncrementMe") != -1:
    		try:
        			newNum = str(int(com[4]) + 1)
    		except ValueError:
        			newNum = ''
    		except IndexError:
        			newNum = ''
    	if(newNum != ''):
        	irc.send("PRIVMSG ".encode("utf-8") + channel.encode("utf-8") + " :Incremented ".encode("utf-8") + newNum.encode('utf-8') + "\n".encode("utf-8"))
