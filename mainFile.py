import sqlite3
import PIL
from PIL import Image, ImageDraw, ImageFont
import getImage
import getLines
from langdetect import detect
import random

conn = sqlite3.connect('test1.db')
curr = conn.cursor()

curr.execute("SELECT * FROM Book1")

rows = curr.fetchall()

count = 0

for row in rows:
    im = PIL.Image.open("background.png")
    draw = ImageDraw.Draw(im)

    
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


    tempStringRow = row[1]

   
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
    file_id=row[2][(findIndex+1):]
    dest = 'output/'+row[0]+'.jpg'
    """mybool2 =True
    countTimes = 0
    while mybool2:
        try:
            
            getImage.download_file_from_google_drive(file_id,dest)
            im2 = PIL.Image.open(dest)
            mybool2 = False
        except:
            print("Error",dest)
            countTimes = countTimes + 1
            print(countTimes)
            if countTimes > 1:
                break
    if mybool2 == True:
        continue"""
    getImage.download_file_from_google_drive(file_id,dest)
    im2 = PIL.Image.open(dest)
        
    if im2.size[1]>im2.size[0]:
        im2 = im2.crop((0,0,im2.size[0],im2.size[0]))
        im2 = im2.resize((440,440))
    else :
        im2 = im2.crop((0,0,im2.size[1],im2.size[1]))
        im2 = im2.resize((440,440))
    im.paste(im2,(180,186))
    im = im.convert("RGB")
    dest = 'output/'+row[0]+str(count)+'.jpg'
    im.save(dest)
    count = count+1
    print(row[0])
