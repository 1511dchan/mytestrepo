#import os
def ls():
    import os
    os.system('lxc-attach -n 1c-it -- ls -lh /root/')

#def hello():
#    print('Hello, world!')

#def fib(n):
#    a = b = 1
#    for i in range(n - 2):
#        a, b = b, a + b
#    return b
