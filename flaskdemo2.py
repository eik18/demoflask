from flask import Flask
import multiprocessing
from time import sleep
from sys import exit

def getqueue(queue2):
    try:
        obj=queue2.get(True,1)
    except Exception as e:
        obj=None  
        pass
        return obj


def runled(queue1):
    end=4
    while True:
        f=getqueue(queue1)
        if f[count] is not None:
            end=f[count]
        for x in range (end):
            print "Counting %d" %(x)
            f=getqueue(queue1)
            if f[flag]=True:
                print "got exit!"
                break

class manageled(object):
    """docstring for manageled"""
    def __init__(self):
        super(manageled, self).__init__()

        self.queue=multiprocessing.Queue()
        self.p = multiprocessing.Process(target=runled, args=(self.queue,))
    def lstart(self):
        h={"count":7,"flag":False}
        self.p.start()
        self.queue.put(h)
    def lstop(self):
        h={'flag':True}
        self.queue.put(h)
        self.queue.close()
        self.queue.join_thread()
        self.p.join


        


app = Flask(__name__)
led=manageled()


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test/<user>")
def reply(user):
    return "Hello %s!" % user
    image = Image.new('RGB', (32, 16))
    draw = ImageDraw.Draw(image) 
    font=ImageFont.truetype("Ubuntu-R.ttf",14)
    draw.text((0,0),user, font=font)
    image.save("%s.jpg" % (user))

@app.route("/start/")
def start():
	#p = multiprocessing.Process(target=runled, args=(queue,))
	#p.start()
    led.lstart()
    return "running"
    
@app.route("/stop/")
def stop ():
    led.lstop()
    return "stop"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
