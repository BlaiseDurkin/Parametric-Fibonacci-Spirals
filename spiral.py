#parametric decaying fib spiral
import graphics
from graphics import *
import math
import time
import moviepy.editor as mpy
import glob
from PIL import Image

pie = math.pi
phi = 1.61803398875
giantlist = []

def takepic(win,i):

    name = "spinpic"
    maxchars = 6
    chars = len(str(i))
    nzeros = maxchars - chars
    soz = nzeros*"0"
    filename = name+soz+str(i)+'.eps'
    win.postscript(file = filename)
    epsfile = Image.open(filename)
    newfilename = filename[:-4]+'.png'
    epsfile.save(newfilename)

def slope_to_ang(dy,dx):
    #arctan(dy,dx) = angle in rad? *180/pi = angle in deg
    if dx == 0:
        if dy > 0:
            return 90
        else:
            return 270
    ang = math.atan(dy/dx)*180/pie
    if dx < 0:
        ang = ang + 180
    if ang < 0:
        ang = 360 + ang
    return ang

def trans(p_c, p_f, theta, wind):
    theta = theta*pie/180

    rad = math.sqrt((p_f.getX() - p_c.getX())**2 + (p_f.getY() - p_c.getY())**2)
    x = rad*math.cos(theta) + p_c.getX()
    y = rad*math.sin(theta) + p_c.getY()
    p_n = Point(x,y)
    return p_n

def SpiralDecay(window, l, length, rotate,s,reverse,img_count):
    '''
        l: length of lines
        length: number of lines in spiral
        rotate: degrees of rotation
        s: spiral iteration
        reverse: bool, true -> mirror spiral
    '''
    x_fr = window.getWidth()//2
    y_fr = window.getHeight()//2
    x_fl = x_fr
    y_fl = y_fr

    pfr = Point(x_fr, y_fr)
    pfl = pfr
    p_c = pfr
    p_f_r = p_c
    tlist_r = []
    tlist_l = []
    p_f_l = p_c


    for t in range(100):
        color = color_rgb(int(255/(.01*t+1)),int(255/(.062*t+1)),int(255/(.01*t+1)))
        #right and left are arbitrary

        x_sr = 1*(l*phi**(-t/10))*math.cos(phi*t/10) + x_fr
        y_sr = 1*(l*phi**(-t/10))*math.sin(phi*t/10) + y_fr
        psr = Point(x_sr, y_sr)

        #get ang
        dy = y_sr - p_c.getY()
        dx = x_sr - p_c.getX()
        ang = slope_to_ang(dy,dx)
        if reverse:
            ang = -1*ang
        #trans
        theta = rotate + ang
        p_n_r = trans(p_c, psr, theta, window)
        tline_r = Line(p_f_r,p_n_r)
        tline_r.setOutline(color)
        tline_r.draw(window)
        giantlist.append(tline_r)
        p_f_r = p_n_r #reset


        #left
        x_sl = -1*(l*phi**(-t/10))*math.cos(phi*t/10) + x_fl
        y_sl = -1*(l*phi**(-t/10))*math.sin(phi*t/10) + y_fl
        psl = Point(x_sl, y_sl)

        #get ang
        dy = y_sl - p_c.getY()
        dx = x_sl - p_c.getX()
        ang = slope_to_ang(dy,dx)

        if reverse:
            ang = -1*ang
        #trans
        theta = rotate + ang
        p_n_l = trans(p_c, psl, theta, window)
        tline_l = Line(p_f_l,p_n_l)
        tline_l.setOutline(color)
        tline_l.draw(window)
        giantlist.append(tline_l)

        p_f_l = p_n_l #reset

        #reset right
        x_fr = x_sr
        y_fr = y_sr
        pfr = psr
        #reset left
        x_fl = x_sl
        y_fl = y_sl
        pfl = psl

        #takepic every 20 iterations
        if t%20 == 0:
            #takepic(window,img_count)
            img_count +=1

    return img_count



def main():
    window = GraphWin("Fib", 500, 500)
    window.setBackground("white")
    initial_length = 40
    duration = 50
    reverse = False
    img_count = 0
    #each iteration length decreases and angle of rotation changes
    for s in range(16):
        rotate = -20*s
        length = initial_length*(1/(1+(math.exp(.3*s-1))))

        img_count = SpiralDecay(window, length, duration, rotate,s,reverse,img_count)
        print(img_count)
    print(img_count," is the img count")

    for i in range(len(giantlist)):
        giantlist[i].undraw()
        if i%30 == 0:
            #takepic(window,img_count)
            img_count +=1

    print(img_count)
    window.getMouse()
    window.close()

main()

def main_2():
    window = GraphWin("Fib", 500, 500)
    window.setBackground("white")
    initial_length = 20
    duration = 50
    reverse = False
    img_count = 0
    #each iteration length decreases and angle of rotation changes
    for s in range(6):
        rotate = 60*s
        if s >2:
            reverse = True

        img_count = SpiralDecay(window, initial_length, duration, rotate,s,reverse,img_count)
        print(img_count)
    print(img_count," is the img count")


    print(img_count)
    window.getMouse()
    window.close()

#main_2()
