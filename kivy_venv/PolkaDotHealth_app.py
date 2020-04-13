import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle

import numpy as np
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
#import bluetooth
import serial
from kivy.lang import Builder
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas
from kivy.garden.matplotlib import FigureCanvasKivyAgg


from PIL import Image
import time
# FIGURE -- Camella's code:
###################################################
xs = [90,200,300,400,500,600,700,800,900,1000,1100,1200]*6
ys = np.array([100,100,100,100,100,100,100,100,100,100,100,100,180,180,180,180,180,180,180,180,180,180,180,180,280,280,280,280,280,280,280,280,280,280,280,280,380,380,380,380,380,380,380,380,380,380,380,380,480,480,480,480,480,480,480,480,480,480,480,480,580,580,580,580,580,580,580,580,580,580,580,580])
colors = ['none']*72
checklist = np.zeros(72)
threshold = 500
colorbank = ['gainsboro','lightpink','pink','crimson','crimson','crimson','crimson','crimson','crimson','crimson']
mapindex = np.array([2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71])
resultsc = colors = ['none']*72
im = np.array(Image.open('bra.png'),dtype=np.uint8)
fig, ax = plt.subplots()
ax.imshow(im)

pmap = ax.scatter(xs, ys, s=400,c=colors,zorder=5)
fig = plt.gcf()

Arduino = serial.Serial('COM9', 9600, timeout=0.5)

###################################################
###################################################
###################################################
###################################################
# SCREENS
class TestScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class ClinicsScreen(Screen):
    pass

class ActiveTestScreen(Screen):
    stopTestCalled = False
    box = BoxLayout()
    bra_plot = FigureCanvasKivyAgg(plt.gcf()) # gets current figure
    def on_enter(self, *args):
        self.stopTestCalled = False
        self.box.size_hint = 0.95, 0.7
        self.box.pos_hint = {"x":0.025, "top":0.9} 
        self.box.add_widget(self.bra_plot)
        self.add_widget(self.box)
        for j in range (0,20):
            for i in (mapindex):
                    f = np.random.rand(1,1)*800
                    colors[i] = colorbank[math.floor(f/100)]
                    #plt.pause(0.001)
            #time.sleep(1)
        pmap.set_color(colors)
        Clock.schedule_interval(self.update_plot, 2) # calls update plot every 2 seconds
    
    # Ideally here we will have the Arduino.read() and use that number to set colors[i]
    def update_plot(self, *args): 
        self.box.remove_widget(self.bra_plot)
        self.remove_widget(self.box)
        box = BoxLayout()
        box.size_hint = 0.95, 0.7
        box.pos_hint = {"x":0.025, "top":0.9} 
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.add_widget(box)
        j = 0
        for i in (mapindex):
            # f = np.random.rand(1,1)*800
            # colors[i] = colorbank[math.floor(f/100)]
            if (self.stopTestCalled):
                break
            Arduino.write(bytes(str(j), 'utf-8'))
            Arduino.write(b"\n")
            while (not Arduino.inWaiting()):# continues if the arduino replies
                pass
            x = Arduino.readline() # maybe switch to Arduino.read(), 
            y = x.decode() # if readline() is switched to read() this may not be necessary anymore
            z = y.rstrip() # if readline() is switched to read() this may not be necessary anymore
            f = math.floor(float(z))
            print(f)
            if f>threshold:
                checklist[i] = 1
            colors[i] = colorbank[math.floor(f/100)]
            j += 1
        pmap.set_color(colors)
    def stopTest(self):
        self.stopTestCalled = True
        Arduino.write(b's')
        
        for i in (mapindex):
            if checklist[i] == 1:
                resultsc[i] = 'crimson'
            if checklist[i] == 0:
                resultsc[i] = 'gainsboro'
            
    pass

class FinishedTestScreen(Screen):
    
    def on_enter(self, *args):
        fig, bx = plt.subplots()
        bx.imshow(im)
        results = bx.scatter(xs, ys, s = 400, c=resultsc)
        box = BoxLayout()
        box.size_hint = 0.95, 0.7
        box.pos_hint = {"x":0.025, "top":0.9}
        finished_plot = FigureCanvasKivyAgg(plt.gcf()) # gets current figure
        box.add_widget(finished_plot)
        self.add_widget(box)
    
    pass

class SerialButton(Widget):
    def connectSerial(self):
        try:
            self.Arduino = serial.Serial('COM9', 9600, timeout=0.5)
        except serial.serialutil.SerialException:
            print("Arduino not connected")
    def turnOn(self): # this is to test with the LED that I have
        # if (self.port.inWaiting()):# if the arduino replies
        #     value = port.readline()# read the reply
        #     print(value)#print so we can monitor it I.e.
        Arduino.write(b"o")
    pass

buildKV = Builder.load_file("PolkaDotHealth.kv")


### MAIN APP ###
class MyApp(App):
    def build(self):
        return buildKV


### RUN ###
if __name__ == '__main__':
    MyApp().run()