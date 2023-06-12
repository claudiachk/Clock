"""
   Claudia Cheuk
   Clock
"""
def setup():
    global reg
    size(800,800)
    frameRate(1)
    rectMode(CENTER)
    reg = createFont("coolvetica.rg-regular copy.otf", 100) #font regularly displayed
    
def draw():
    #setup variables in draw so that it will update according to the time
    h = hour()
    m = minute()
    s = second()
    d = day()
    mo = month()
    y = year()
    
    translate(0,height/8)
    textFont(reg)     
    textAlign(CENTER, CENTER)
    noStroke()
    push()
    
    #background color based on hours
    if h <= 4:
        background(0,2,32)
    elif h <= 6:
        background(241, 179, 81)
    elif h < 12:
        background(255, 227, 167)
    elif h <= 16:
        background(255,210,127)
    elif h <= 18:
        background(240,101,83)
    elif h <= 20:
        background(107, 73, 132)
    else:
        background(16,62,105)
        
    #minutes
    textSize(150)
    if h > 6 and h < 12:
        fill(85,60,40)
    else:
        fill(240)
    if m < 10:
        x = width/4+195
        text(0, x, height/8+45)
        text(m,x+75,height/8+45)
    else:
        text(m, width/4+230, height/8+45)

    
    #seconds
    if h > 6 and h < 12:
        fill(108, 81, 60)
    else:
        fill(230)
    if s < 10:
        x = width*3/4+15
        text(0, x, height/8+45)
        text(s,x+75,height/8+45)
    else:
        text(s, width*3/4+50, height/8+45)
    
    #date
    textSize(60)
    if mo == 1:
        moName = "JAN"
    elif mo == 2:
        moName = "FEB"
    elif mo == 3:
        moName = "MAR"
    elif mo == 4:
        moName = "APR"
    elif mo == 5:
        moName = "MAY"
    elif mo == 6:
        moName = "JUN"
    elif mo == 7:
        moName = "JUL"
    elif mo == 8:
        moName = "AUG"
    elif mo == 9:
        moName = "SEP"
    elif mo == 10:
        moName = "OCT"
    elif mo == 11:
        moName = "NOV"
    else:
        moName = "DEC"
    fill(255,0,0,99)   
    text(moName,width*3/4+20,height/2-105)
    text(d, width*3/4+100,height/2-105)
    text(y,width*3/4+30,height/2-55)
    if (h > 6 and h < 12) or (h==17 or h==18):
        fill(62,39,21,50)
    else:
        fill(255,255,255,50)   
    text(moName,width*3/4+20,height/2-105)
    text(d, width*3/4+100,height/2-105)
    text(y,width*3/4+30,height/2-55)
    
     #hours
    textSize(150)
    if h < 12 and h >= 0:
        if h <= 6:
            fill(255)
        elif h > 6 and h < 12:
            fill(62,39,21)
        text("AM",width/4+255, height/2-88)
    else:
        fill(255)
        if h > 12:
           h = h - 12
        textSize(150)
        text("PM", width/4+255, height/2-88)
    if h == 0:
        h =+ 12
    textSize(50)
    text("Have a good day.", width/2, height*2/3)
    textSize(400)     
    text(h, width/4-20, height/4+20)
    
    #flashing dots
    if s % 2 == 0:
        fill(255,0,0,90)
    else:
        noFill()
        stroke(255,0,0,90)
        strokeWeight(3)
    ellipse(width/2-75, height/8+77,55,55) #bottom
    ellipse(width/2+140, height/8+25,55,55) #top
