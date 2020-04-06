# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:14:51 2020

@author: Camella
"""

import numpy as np
import matplotlib.animation as animation
import math
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
import serial
import time

#Arduino = serial.Serial('COM5', 9600, timeout=0.5)


#data = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
xs = [90,200,300,400,500,600,700,800,900,1000,1100,1200]*6
ys = np.array([100,100,100,100,100,100,100,100,100,100,100,100,180,180,180,180,180,180,180,180,180,180,180,180,280,280,280,280,280,280,280,280,280,280,280,280,380,380,380,380,380,380,380,380,380,380,380,380,480,480,480,480,480,480,480,480,480,480,480,480,580,580,580,580,580,580,580,580,580,580,580,580])
colors = ['none']*72
colorbank = ['gainsboro','lightpink','pink','crimson','crimson','crimson','crimson','crimson','crimson','crimson']
mapindex = np.array([2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71])
#nulls (35,36,47,48,49,58,59,60,61,70,71)

#im = np.array(Image.open('bra_2.png'),dtype=np.uint8)


fig, ax = plt.subplots()
#ax.imshow(im)

pmap = ax.scatter(xs, ys, s=400,c=colors,zorder=5)
fig = plt.gcf()
fig.show()


#def plot(data):
#while True: 
for j in range (0,20):
        #data[i%4][math.floor(i%16/4)] = np.random.rand(1,1)
    for i in (mapindex):
            #while (not Arduino.inWaiting()):# if the arduino replies
             #   pass
            #x = Arduino.readline()
            #y = x.decode()
            #z = y.rstrip()
            #f = math.floor(float(z))
            f = np.random.rand(1,1)*800
            colors[i] = colorbank[math.floor(f/100)]
            plt.pause(0.001)
    #time.sleep(1)
    pmap.set_color(colors)
