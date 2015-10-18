#import os
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
    print out


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
    print "Corbina host adress is "+host



#def hello():
#    print('Hello, world!')

#def fib(n):
#    a = b = 1
#    for i in range(n - 2):
#        a, b = b, a + b
#    return b
