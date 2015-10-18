#!/usr/bin/python
import lxc

c = lxc.Container("voip")
if not c.running:
    c.start()

def print_hostname():
    with open("/etc/hostname", "r") as fd:
        print("Hostname: %s" % fd.read().strip())

# первый запуск в хостовой системе
print_hostname()

# запуск в контейнере - гостевая система
c.attach_wait(print_hostname)

#if not c.shutdown(30):
#    c.stop()
