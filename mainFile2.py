import sqlite3
import PIL
from PIL import Image, ImageDraw, ImageFont
import getImage
import getLines
from langdetect import detect
import random


row = ["Manish","Positive attitude and I get on well with all kinds of people.","https://drive.google.com/open?id=1zerefs55fWg8DJ4e_1i4WuzIyRW-1wud"]
im = PIL.Image.open("background.png")
draw = ImageDraw.Draw(im)

if detect(row[0]) == "mr":
    inFont = "Mukta.ttf"
else:
    inFont = "CooperHewitt-BoldItalic.otf"

i=40
myBool = True
myFont = ImageFont.truetype(inFont, i)

checkLight = 601
while checkLight > 600:
    randomRed = random.randint(0,255)
    randomBlue = random.randint(0,255)
    randomGreen = random.randint(0,255)
    checkLight = randomRed + randomGreen + randomBlue
    RGB = (randomRed,randomBlue,randomGreen)

tempString="HEY "+row[0].upper()+","

while myBool:
    w,h = draw.textsize(tempString,font=myFont)
    w2,h2 = draw.textsize("HEY ,",font=myFont)
    if w<360:
        draw.text(((800-w)/2,95),"HEY ", (40,11,93) , font = myFont)
        draw.text((((800-w)/2)+w2,95),row[0].upper()+",", RGB, font = myFont)
        myBool = False
    else :
        i = i-2
        myFont = ImageFont.truetype("CooperHewitt-BoldItalic.otf", i)


tempStringRow = "\""+row[1]+"\""

if detect(row[1]) == "mr":
    inFont = "Mukta.ttf"
else:
    inFont = "CooperHewitt.otf"

i = 40
myFont = ImageFont.truetype(inFont, i)
lines = getLines.text_wrap(tempStringRow,myFont,488)
w1,h1 = draw.textsize(tempString,font=myFont)

noOfLines = len(lines)

while noOfLines >= 4:
    myFont = ImageFont.truetype(inFont, i)
    lines = getLines.text_wrap(tempStringRow,myFont,488)
    w1,h1 = draw.textsize(tempString,font=myFont)
    noOfLines = len(lines)
    i = i - 2

if noOfLines == 1:
    w1,h1 = draw.textsize(lines[0],font=myFont)
    draw.text(((800-w1)/2,680),lines[0],(40,11,93), font = myFont)
elif noOfLines == 2:
    w1,h1 = draw.textsize(lines[0],font=myFont)
    draw.text(((800-w1)/2,(680-16)),lines[0],(40,11,93), font = myFont)
    w1,h1 = draw.textsize(lines[1],font=myFont)
    draw.text(((800-w1)/2,(680+30)),lines[1],(40,11,93), font = myFont)
elif noOfLines == 3:
    w1,h1 = draw.textsize(lines[0],font=myFont)
    draw.text(((800-w1)/2,(665-16)),lines[0],(40,11,93), font = myFont)
    w1,h1 = draw.textsize(lines[1],font=myFont)
    draw.text(((800-w1)/2,(665+30)),lines[1],(40,11,93), font = myFont)
    w1,h1 = draw.textsize(lines[2],font=myFont)
    draw.text(((800-w1)/2,(665+76)),lines[2],(40,11,93), font = myFont)


findIndex = row[2].index("=")
idAdd=row[2][(findIndex+1):]
dest = 'output/'+row[0]+'.jpeg'
print(dest)
mybool2 =True
countTimes = 0
while mybool2:
    try:
        idAdd=row[2][(findIndex+1):]
        print(idAdd)
        getImage.download_file_from_google_drive(idAdd,dest)
        im2 = PIL.Image.open(dest)
        mybool2 = False
        print("Done")
    except:
        print("Error")
        countTimes = countTimes + 1
        print(countTimes)
        if countTimes > 50:
            break


im2 = PIL.Image.open(dest)
im2 = im2.transpose(Image.ROTATE_90)
im2 = im2.transpose(Image.ROTATE_90)
im2 = im2.transpose(Image.ROTATE_90)
print(im2.size)    
if im2.size[1]>im2.size[0]:
    im2 = im2.crop((0,0,im2.size[0],im2.size[0]))
    im2 = im2.resize((440,440))
else :
    im2 = im2.crop((0,0,im2.size[1],im2.size[1]))
    im2 = im2.resize((440,440))
im.paste(im2,(180,186))
im = im.convert("RGB")
dest = 'output/'+row[0]+'.jpeg'
im.save(dest)

