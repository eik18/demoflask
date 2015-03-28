import multiprocessing
from time import sleep

def f(q):
    while True:
        try:
            obj=q.get(True,1)
        except Exception as e:
            obj=None  
        if obj is not None:
            break
    	print "No flag"
    print "got flag!"
    

if __name__ == '__main__':
    queue=multiprocessing.Queue()
    p = multiprocessing.Process(target=f, args=(queue,))
    p.start()
    sleep (5)
    queue.put('something')
    queue.close()
    queue.join_thread()
    p.join
 