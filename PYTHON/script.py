#!/usr/bin/python

#login = raw_input("Enter your name: ")

#gogo = open ("/home/neon/helloworld","w")
#gogo.write("Hello, world!")
#gogo.close()

import os
import re
vid = os.popen("host l2tp.corbina.ru")
re_dns = re.compile(r"([\d]+)\.([\d]+)\.([\d]+)\.([\d]+)")
for line in vid.readlines():
  hst=re_dns.search(line)
  if (hst != None):
    break
host=hst.group(0)
print "Corbina host adress is "+host
