#import os
def prun():
    from subprocess import Popen, PIPE
#    from os import chdir
    import os, glob
#    proc = Popen("ls -lh", shell=True, stdout=PIPE, stderr=PIPE)
#    Popen("ls -lh", shell=True)
    dns_zone="cs.cln.su"
    os.chdir("/var/cache/bind/dnssec/"+dns_zone)
#    Popen("dnssec-keygen -a RSASHA1 -b 1024 -n ZONE cs.cln.su", shell=True).wait()
#    Popen("dnssec-keygen -a RSASHA1 -b 2048 -f KSK -n ZONE cs.cln.su", shell=True).wait()
#    Popen("dnssec-signzone -S -N INCREMENT cs.cln.su", shell=True).wait()
#    Popen("rm Kcs.cln.su*", shell=True)
#    import glob
    for filename in glob.glob("K"+dns_zone+"*"):
        print (filename)
#        os.remove(filename)
#    Popen("dnssec-keygen -a RSASHA1 -b 1024 -n ZONE cs.cln.su", shell=True)
#    Popen("dnssec-keygen -a RSASHA1 -b 2048 -f KSK -n ZONE cs.cln.su", shell=True)
#    Popen("dnssec-signzone -S -N INCREMENT cs.cln.su", shell=True)
#    Popen("pwd", shell=True, stdout=PIPE, stderr=PIPE)
#    proc.wait()    # дождаться выполнения
#    res = proc.communicate()  # получить tuple('stdout res', 'stderr res')
#    if proc.returncode:
#        print (res[1])
#    print ('result:', res[0])

#    print (proc.stdout.read())

def ls():
#    import os
#    os.system('lxc-attach -n 1c-it -- ls -lh /root/')
#    Popen("lxc-attach -n test -- ls -lh /root/" + "", shell=True).wait()

    from subprocess import Popen, PIPE
#p = subprocess.Popen(['ls -lh'], stdout=subprocess.PIPE)
#p = subprocess.Popen("ls -lh", shell=True, stdout=subprocess.PIPE)
#    sp = subprocess
    p = Popen("lxc-attach -n 1c-it -- ls -lh /root/", shell=True, stdout=PIPE)
    out = p.stdout.read()
    print (out)


def ip():
    from subprocess import Popen, PIPE
    import re

#    sp = subprocess
    vid = Popen("host l2tp.corbina.ru", shell=True, stdout=PIPE)
    re_dns = re.compile(r"([\d]+)\.([\d]+)\.([\d]+)\.([\d]+)")
    for line in vid.stdout:
        hst=re_dns.search(line)
        if (hst != None):
            break
    host=hst.group(0)
    print ("Corbina host adress is "+host)

def DnsSec(dns_zone_name):
    from subprocess import Popen, PIPE
    import os, glob, linecache, re, time

   line = linecache.getline(dns_root_dir+dns_zone_name+"/dsset-"+dns_zone_name+".").partition("DS")
   print(line[0])
#    linecache.getline(dns_root_dir+"cs.cln.su/"+dns_zone_name,1)[-3:-1]













