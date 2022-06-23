import serial
import tkinter as tk

arduino=serial.Serial('com4',baudrate=9600)

def led_on():
    arduino.write(b'1')
    print('led_on')
def led_off():
    arduino.write(b'0')
    print('led_off')

root=tk.Tk()

bt1=tk.Button(root,text='bat',command=led_on)
bt2=tk.Button(root,text='tat',command=led_off)

bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)
root.geometry('200x300')
root.mainloop()