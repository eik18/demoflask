from PIL import Image, ImageDraw,ImageFont
text='test3'
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image) 
font=ImageFont.truetype("Ubuntu-R.ttf",14)
draw.text((0,0),text, font=font)
#image.show()
image.save("%s.jpg" % (text))