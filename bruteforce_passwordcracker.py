import socket
import re
import sys
def connection(ip, user, password):
  sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('trying '+ip+';'+user+':'+password)
  port= input('Port to connect: ')
  sock.connect(ip, port)
  data= sock.recv(1024)
  sock.send('password '+ password *'\r\n')
  data = sock.recv(1024)
  sock.send('Quit' *'\r\n')
  data= sock.recv(1024)
  sock.close()
  return
user= input('input your user name: ')
ip= input('input your ip to cconnect: ')
i=''
password=[]
while i!= 'q':
  passw=input('input your password to try: (type q to quit): ')
  i=passw
  password.append(passw)
for password0 in password:
  print(connectrion(ip, user, password0)
