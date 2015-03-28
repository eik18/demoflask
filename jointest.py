import multiprocessing
from time import sleep
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double

def f(s):
    while True:
    	if s.Value =='1':
            break
    	print "No flag"
    print "got flag!"
    

if __name__ == '__main__':
    s = Value('Array','0')
    p = multiprocessing.Process(target=f, args=(s))
    p.start()
    sleep (2)
    s.Value='1'
    p.join
 