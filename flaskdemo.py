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

app = Flask(__name__)
queue=multiprocessing.Queue()
p = multiprocessing.Process(target=runled, args=(queue,))

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
	p.start()
	return "running"
    
@app.route("/stop/")
def stop ():
    queue.put('something')
    queue.close()
    queue.join_thread()
    p.join
    return "stop"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
