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


from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas
from kivy.garden.matplotlib import FigureCanvasKivyAgg

class TestScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

fig, ax = plt.subplots()
canvas = fig.canvas


#############################################################################################

def enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()


class Test(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.add_plot()

    def get_fc(self, i):
        fig1 = plt.figure()
        fig1.suptitle('mouse hover over figure or axes to trigger events' +
                      str(i))
        ax1 = fig1.add_subplot(211)
        ax2 = fig1.add_subplot(212)
        wid = FigureCanvas(fig1)
        fig1.canvas.mpl_connect('figure_enter_event', enter_figure)
        fig1.canvas.mpl_connect('figure_leave_event', leave_figure)
        fig1.canvas.mpl_connect('axes_enter_event', enter_axes)
        fig1.canvas.mpl_connect('axes_leave_event', leave_axes)
        return wid

    def add_plot(self):
        btn = Button()
        self.add_widget(btn)
        self.add_widget(self.get_fc(1))
#############################################################################################




class ActiveTestScreen(Screen):
    def on_enter(self, *args):
        box = BoxLayout()
        box.size_hint = 0.95, 0.7
        box.pos_hint = {"x":0.025, "top":0.9} 
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.add_widget(box)

    def startTest(self):
        self.box = BoxLayout()
        fig1 = plt.figure()
        fig1.suptitle('mouse hover over figure or axes to trigger events')
        ax1 = fig1.add_subplot(211)
        ax2 = fig1.add_subplot(212)
        wid = FigureCanvas(fig1)
        fig1.canvas.mpl_connect('figure_enter_event', enter_figure)
        fig1.canvas.mpl_connect('figure_leave_event', leave_figure)
        fig1.canvas.mpl_connect('axes_enter_event', enter_axes)
        fig1.canvas.mpl_connect('axes_leave_event', leave_axes)
        self.box.add_widget(wid)
        # self.i = 0
        # self.line = [self.i]
        # self.add_widget(canvas)
        # #plt.show()
        # Clock.schedule_interval(self.update, 1)
        #self.add_plot()

    def update(self, *args):
        plt.plot(self.line, self.line)
        self.i += 1
        self.line.append(self.i)
        canvas.draw_idle()
    
    def get_fc(self, i):
        fig1 = plt.figure()
        fig1.suptitle('mouse hover over figure or axes to trigger events' +
                      str(i))
        ax1 = fig1.add_subplot(211)
        ax2 = fig1.add_subplot(212)
        wid = FigureCanvas(fig1)
        fig1.canvas.mpl_connect('figure_enter_event', enter_figure)
        fig1.canvas.mpl_connect('figure_leave_event', leave_figure)
        fig1.canvas.mpl_connect('axes_enter_event', enter_axes)
        fig1.canvas.mpl_connect('axes_leave_event', leave_axes)
        return wid

    def add_plot(self):
        self.add_widget(self.get_fc(1))
        self.add_widget(self.get_fc(2))

    pass

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



# fig, ax = plt.subplots()
# canvas = fig.canvas

buildKV = Builder.load_file("my.kv")


### MAIN APP ###
class MyApp(App):
    def build(self):
        return buildKV


### RUN ###
if __name__ == '__main__':
    MyApp().run()