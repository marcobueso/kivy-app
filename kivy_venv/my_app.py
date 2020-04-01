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
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import matplotlib.pyplot as plt
import bluetooth
import serial
from kivy.lang import Builder


class TestScreen(Screen):
    # def __init__(self, **kwargs):
    #     self.box = BoxLayout()
    #     self.i = 0
    #     self.line = [self.i]
    #     self.box.add_widget(canvas)
    #     #plt.show()
    #     Clock.schedule_interval(self.update, 0.1)
    #     self.add_widget(canvas)

    # def update(self, *args):
    #     plt.plot(self.line, self.line)
    #     self.i += 1
    #     self.line.append(self.i)
    #     canvas.draw_idle()
    
    pass

class HomeScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(HomeScreen, self).__init__(**kwargs)
    #     #self.BTbutton = BluetoothButton()
    #     #self.add_widget(self.BTbutton)
    #     self.SButton = SerialButton()
    #     self.add_widget(self.SButton)

class BluetoothButton(Widget):
    def __init__(self, **kwargs): 
        #super is parent class        
        super(BluetoothButton, self).__init__(**kwargs) 
  
        # creating Button     
        BTbtn = Button(text ='Connect to Bluetooth Devices', font_size ="15sp", 
                    background_color =(1, 1, 1, 1), 
                    color =(1, 1, 1, 1),  
                    size =(300, 32),  
                    # size_hint =(.2, .2),  
                    pos =(300, 250))  

        # Arranging a callback
        BTbtn.bind(on_press = self.callback) 
        self.add_widget(BTbtn) 
    
    def callback(self, instance): # called when pressed
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("Found {} devices.".format(len(nearby_devices)))
        devices_list = ""
        for addr, name in nearby_devices:
            print("  {} - {}".format(addr, name))
            devices_list += "  {} - {}".format(addr, name)
        

class SerialButton(Widget):
    port = serial.Serial('COM9', 9600, timeout=0.5)
    def connectSerial(self):
        try:
            self.port = serial.Serial('COM9', 9600, timeout=0.5)
        except serial.serialutil.SerialException:
            print("Arduino not connected")
    def turnOn(self):
        # if (self.port.inWaiting()):# if the arduino replies
        #     value = port.readline()# read the reply
        #     print(value)#print so we can monitor it I.e.
        self.port.write(b"1")
        print("Wrote 1 to port")
    pass
    # def __init__(self, **kwargs): 
    #     #super is parent class        
    #     super(SerialButton, self).__init__(**kwargs) 
  
    #     # creating Button     
    #     SerialBtn = Button(text ='Connect to Serial Port', font_size ="15sp", 
    #                 background_color =(1, 1, 1, 1), 
    #                 color =(1, 1, 1, 1),  
    #                 size =(300, 32),  
    #                 # size_hint =(.2, .2),  
    #                 pos =(300, 250))  

    #     # Bind a callback
    #     SerialBtn.bind(on_press = self.callback) 
    #     self.add_widget(SerialBtn)
    
    # def callback(self, instance): # called when pressed
    #     #create the serial port object
    #     try:
    #         sm.current = 'test'
    #         port = serial.Serial('COM9', 115200, timeout=0.5)

    #     except serial.serialutil.SerialException:
    #         print("Arduino not connected")
        # if (port.inWaiting()):# if the arduino replies
        #     value = port.readline()# read the reply
        #     print(value)#print so we can monitor it I.e.
        #     if (value.strip().isdigit()):
        #         number = int(float(value.strip())) #convert received data to integer
        #         print('Channel 0: {0}'.format(number))

class Sensor(Widget):
    pass
    def update(self):
        #TODO update color
        return 0



fig, ax = plt.subplots()
canvas = fig.canvas

# Create the screen manager
sm = ScreenManager()
# Create n screens --TODO: right now we will only have 2: "home", and "start test" pages
sm.add_widget(HomeScreen(name = "home"))
sm.add_widget(TestScreen(name = "test"))


buildKV = Builder.load_file("my.kv")


class MyApp(App):

    def build(self):
        # simple inquiry example
        
        #btn = BluetoothButton()
        #return Label(text = devices_list)
        #return Label(text='Hello world')
        #box = BoxLayout()
        # self.i = 0
        # self.line = [self.i]
        #box.add_widget(canvas)
        #box.add_widget(btn)
        # #plt.show()
        # Clock.schedule_interval(self.update, 0.1)
        # return box

        return buildKV
        #sm# -- TODO


        




if __name__ == '__main__':
    MyApp().run()