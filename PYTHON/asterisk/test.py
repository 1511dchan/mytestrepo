#!/usr/bin/python

#login = raw_input("Enter your name: ")

#gogo = open ("/home/neon/helloworld","w")
#gogo.write("Hello, world!")
#gogo.close()

import mod_sys as sys

#os.system('ls -lh')
#os.system('lxc-attach -n 1c-it -- ls -lh /root/')
sys.ls()
sys.ip()

#import subprocess
#import re
#p = subprocess.Popen(['ls -lh'], stdout=subprocess.PIPE)
#p = subprocess.Popen("ls -lh", shell=True, stdout=subprocess.PIPE)
#sp = subprocess
#p = sp.Popen("lxc-attach -n 1c-it -- ls -lh /root/", shell=True, stdout=sp.PIPE)
#out = p.stdout.read() 
#print out


#vid = subprocess.Popen("host l2tp.corbina.ru", shell=True, stdout=subprocess.PIPE)
#re_dns = re.compile(r"([\d]+)\.([\d]+)\.([\d]+)\.([\d]+)")
#for line in vid.stdout:
#  hst=re_dns.search(line)
#  if (hst != None):
#    break
#host=hst.group(0)
#print "Corbina host adress is "+host
