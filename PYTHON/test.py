#!/usr/bin/python

#apt-get update && apt-get -y install python-pip
#pip install pexpect

#converted from: http://pexpect.sourceforge.net/pexpect.html
#child = pexpect.spawn('scp foo myname@host.example.com:.')
#child.expect ('Password:')
#child.sendline (mypassword)
import pexpect
import sys
user=sys.argv[1]
passwd=sys.argv[2]
child = pexpect.spawn('/usr/bin/smbpasswd -a '+str(user))
child.expect('New SMB password:')
child.sendline (passwd)
child.expect ('Retype new SMB password:')
child.sendline (passwd)
