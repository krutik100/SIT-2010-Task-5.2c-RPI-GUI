from tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from functools import partial
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
 
def selection():
    
    if(radioValue.get() == 1):
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
    elif (radioValue.get() ==2):
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
    elif (radioValue.get() ==3):
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
    elif (radioValue.get() ==4):
        print ("sorry there is nor radiobutton")
def test():
    print('clean')
    GPIO.cleanup()
    quit()
    
frame = Tk()  
frame.geometry("350x350")  
radioValue = IntVar()
title = Label(text = "Choose a colour to on LED:")  
title.pack()

    
radio1 = Radiobutton(frame, text="GREEN", variable=radioValue, value=1,  
      command=selection)

radio1.pack( anchor = N )  
  
radio2 = Radiobutton(frame, text="RED", variable=radioValue, value=2,  
                  command=selection)  
radio2.pack( anchor = N )  
  
radio3 = Radiobutton(frame, text="YELLOW", variable=radioValue, value=3,  
                  command=selection)  
radio3.pack( anchor = N)

B1=Button(frame, text='EXIT', command=partial(test))
B1.pack( anchor = CENTER)


label = Label(frame)  
label.pack()  
frame.mainloop()  

