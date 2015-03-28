import multiprocessing
from time import sleep
from sys import exit

def g(u):
    for x in range (10):
        print "Counting %d" %(x)
        try:
            obj=u.get(True,1)
        except Exception as e:
            obj=None  
            pass
        if obj is not None:
            print "got exit!"
            exit()

def f(q):
    while True:
        print "start while"
        g(q)
        
    

if __name__ == '__main__':
    queue=multiprocessing.Queue()
    p = multiprocessing.Process(target=f, args=(queue,))
    p.start()
    sleep (25)
    queue.put('something')
    queue.close()
    queue.join_thread()
    p.join
 