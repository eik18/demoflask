from multiprocessing import Process, Pipe
from time import sleep

def f(conn):
    flag={}
    while True:
        flag=conn.recv()
        if flag is empty:
            print "nothing"
        else:
            print flag["test"]
    

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    sleep (5)
    flag={"test":"true",}
    parent_conn.send(flag)   # prints "[42, None, 'hello']"
    parent_conn.close()
    p.join
 