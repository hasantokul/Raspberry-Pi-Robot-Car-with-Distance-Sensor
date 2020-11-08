import RPi.GPIO as gpio
import time
from tkinter import *

gpio.setmode(gpio.BOARD)

class Car():
    
    def __init__(self,master):
        
        frame = Frame(master)
        frame.pack()
        master.bind("<KeyPress>",self.key_input)
        
    def distance(self):
        
        gpio.setup(12,gpio.OUT)
        gpio.setup(16,gpio.IN)

        gpio.output(12, False)
        
        gpio.output(12, True)
        time.sleep(0.00001)
        gpio.output(12, False)

        while gpio.input(16) == 0:
            pulse_start = time.time()

        while gpio.input(16) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17150
        
        return distance
        
    def setgpio(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11,gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        
    
    def forward(self,tf):
            
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13 ,True)
        gpio.output(15, False)
        time.sleep(tf)
        gpio.cleanup()
        
    def reverse(self,tf):

        gpio.output(7,True)
        gpio.output(11,False)
        gpio.output(13,False)
        gpio.output(15,True)
        time.sleep(tf)
        gpio.cleanup()
        
    def turn_left(self,tf):

        gpio.output(7,True)
        gpio.output(11,False)
        gpio.output(13,True)
        gpio.output(15,False)
        time.sleep(tf)
        gpio.cleanup()
        
    def turn_right(self,tf):

        gpio.output(7, False)
        gpio.output(11,True)
        gpio.output(13,False)
        gpio.output(15,True)
        time.sleep(tf)
        gpio.cleanup()   

    def key_input(self,event):
        
        try:
            self.setgpio()
            print("Key", event.char)
            
            key_press = event.char
            
            sleep_time = 0.030
            
            print(self.distance())
            
            
            if key_press.lower() == "w":
                self.forward(sleep_time) 
            
            elif key_press.lower() == "s":
                self.reverse(sleep_time)
            
            elif key_press.lower() == "a":
                self.turn_left(sleep_time)
            
            elif key_press.lower() == "d":
                self.turn_right(sleep_time)
        
        except UnboundLocalError:
            gpio.cleanup()
            
        
root1 = Tk()
root = Tk()
app = EezyBotArm(root)
app1 = Car(root1)
root.geometry("290x270+0+0")
root1.geometry("200x200+300+40")
root1.mainloop()
root.mainloop()
