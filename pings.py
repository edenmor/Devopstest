import os

file=open('servers.txt','r')
lines = file.readlines()
response=0
with open ('servers.txt') as datafile:
  for hostname in datafile: 
    response = os.system("ping -c 1 " + hostname)
    if response ==0:
     print hostname , 'is up!'
    else:
     print hostname, 'is down!'
