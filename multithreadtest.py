from multiprocessing import Process, Pipe
from time import sleep

def f(conn):
    flag="false"
    while flag == "false":
    	flag=conn.recv()
    	print "No flag"
    print "got flag!"
    

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    sleep (5)
    flag="true"
    parent_conn.send([flag])   # prints "[42, None, 'hello']"
    parent_conn.close()
    p.join
 