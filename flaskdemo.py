from flask import Flask
import multiprocessing
from time import sleep
from sys import exit

def runtext(queue1):
    for x in range (10):
        print "Counting %d" %(x)
        try:
            obj=queue1.get(True,1)
        except Exception as e:
            obj=None  
            pass
        if obj is not None:
            print "got exit!"
            exit()

def runled(queue2):
    while True:
        print "start while"
        runtext(queue2)

class manageled(object):
    """docstring for manageled"""
    def __init__(self):
        super(manageled, self).__init__()

        self.queue=multiprocessing.Queue()
        self.p = multiprocessing.Process(target=runled, args=(self.queue,))
    def lstart(self):
        self.p.start()
    def lstop(self):
        self.queue.put('something')
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
