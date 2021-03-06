from flask import Flask
import multiprocessing
from time import sleep
from sys import exit

def getqueue(queue2):
    try:
        obj=queue2.get(True,1)
        print "not dict"
        #print obj
        return obj
    except Exception as e:
        obj={'nothing':'none'}
        return obj


class runled(object):
    """docstring for runled"""
    def __init__(self):
        super(runled, self).__init__()
        #self.queue = internalqueue
        self.defaulttext="test"
    def runtext(self,queue):
        temptext=self.defaulttext
        while True:
            for x in range (10):
                print "Counting %d, text is %s" %(x,temptext)
                obj=getqueue(queue)
                if 'flag' in obj and obj["flag"]==True:
                    print "got exit!"
                    exit()
                if 'text' in obj:
                    temptext=obj['text']



class manageled(object):
    """docstring for manageled"""
    def __init__(self):
        super(manageled, self).__init__()

        self.queue=multiprocessing.Queue()
        led=runled()
        self.p = multiprocessing.Process(target=led.runtext,args=(self.queue,))  #call queue here
    def lstart(self):
        self.p.start()
    def lstop(self):
        temphash={"flag":True}
        #temphash={"text":"work?"}
        self.queue.put(temphash)
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
