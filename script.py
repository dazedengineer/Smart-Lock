import RPi.GPIO as gpio # importing library to use GPIO pins
import time
from tkinter import * #importing Tkinter for creating GUI
servo=32 #assignment of signal pin of servo to pin32 which is a PWM pin

root=Tk()
root.geometry('1280x720') # assigning dimensions of the window using geometry library
root.title("SMART LOCK") # title is given
def Lock(): #function called lock is defined
print("Lock")
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(servo,gpio.OUT) # pin 32 is set as output pin.
pwm=gpio.PWM(servo,50) # 50 hz of frequency is assigned to servo
pwm.start(0)
gpio.output(servo,True) #condition true makes it rotate by 90 degrees
pwm.ChangeDutyCycle(7)
time.sleep(1) # delay
gpio.output(servo,False) # if condition not met the servo does not rotate
pwm.ChangeDutyCycle(0)
pwm.stop()
gpio.cleanup()
def Unlock(): # function called unlock is defined
global wrong
unlock['state']=DISABLED # state of unlock button is disabled till the following code is executed
Pass=inp.get() # creating a variable pass to get input
if Pass == "pi": # password to unlock the door is created
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(servo,gpio.OUT) # pin 32 is set as output pin.
pwm=gpio.PWM(servo,50) # 50hz of frequency is assigned to servo
pwm.start(0) # start PWM
gpio.output(servo,True) # If true, servo rotates to 90 degrees
pwm.ChangeDutyCycle(2)
time.sleep(1) # delay created
gpio.output(servo,False) # if condition not met the servo does not rotate
pwm.ChangeDutyCycle(2)
pwm.stop() #stop PWM
gpio.cleanup()
#clears the port 32 and makes it ready to receive next instruction
succ = Label(root,text="Unlocked")
succ.pack(padx=1,pady=3)
unlock['state']=NORMAL
# after password is entered, the unlock button is bought to normal state #so that on the press of the but
ton the door is unlocked
else:

wrong = Label(root,text="Wrong Passcode try again")
# it prints the text if the password entered is wrong
wrong.pack(padx=1,pady=3)
time.sleep(2)
unlock['state']=NORMAL
lock= Button(root,text="Lock", command=Lock, padx=30,pady=30,width=30,bg='violet')
# button is a widget in tkinter which has paramters like command, #dimensions, background color, text col
or etc.
lock.pack(padx=1,pady=2)
inp=Entry(root,width=20)
# entry is a another widget in Tkinter that creates an input entry field for the user
inp.pack(padx=0,pady=1)
inp.insert(0,"")
unlock= Button(root,text="Unlock",command=Unlock,padx=20,
pady=30,width=30,bg="green")
# unlock button is created with its parametres defined
unlock.pack(padx=1,pady=1)
root.mainloop()
# this code keeps looping