import configparser
import tkinter as tk
from tkinter import messagebox

config = configparser.ConfigParser()

win = tk.Tk()
win.title("KodPixel-X-Second-Timer")
win.geometry("520x570")

global red1

red1 = win.config(bg="red")
config['settings'] = {
       'color': 'red'
   }

with open ('Settings.ini', 'w') as f:
    config.write(f)

def about():
   messagebox.showinfo("KodPixel-X-Second-Timer", "This is a Second Timer.")


config.read('Settings.ini')
color = config.get('settings', 'color')

if color == "red":
    win.config(bg="red")

elif color == "green":
    win.config(bg="green")

elif color == "yellow":
    win.config(bg="yellow")

elif color == "blue":
    win.config(bg="blue")

label = tk.Label(win, text="0", font=("Arial", 25))
label.pack(pady=20)

def plus():
    ButtonBool = True
    if ButtonBool == True:
        current = int(label.cget("text"))
        label.config(text=str(current + 1))
        global winafter
        winafter = win.after(1000, plus)
        winafter()

def Pause():
    global ButtonBool
    ButtonBool = False    
    winafter2 = win.after_cancel(winafter)
    winafter2()
    label.config(text="0")

def Stop():
    global ButtonBool
    ButtonBool = False   
    label.config(text="0") 
    winafter2 = win.after_cancel(winafter)
    winafter2()


def blue():
    global blue
    blue = win.config(bg="blue")

    config['settings'] = {
       'color': 'blue'
    }

    with open ('Settings.ini', 'w') as f:
     config.write(f)


def red():
    global red
    red = win.config(bg="red")
    config['settings'] = {
       'color': 'red'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)

def green():
    global green
    green = win.config(bg="green")
    config['settings'] = {
       'color': 'green'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)
    

def yellow():
    global yellow
    yellow = win.config(bg="yellow")
    config['settings'] = {
       'color': 'yellow'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)

    

button = tk.Button(win, text="Start", command=plus)
button.pack(pady=10)

buttonb = tk.Button(win, text="Make the background color blue.", command=blue)
buttonb.pack()

buttonr = tk.Button(win, text="Make the background color red.", command=red)
buttonr.pack()

buttong = tk.Button(win, text="Make the background color green.", command=green)
buttong.pack()

buttony = tk.Button(win, text="Make the background color yellow.", command=yellow)
buttony.pack()

buttonPause = tk.Button(win, text="Pause", command=Pause)
buttonPause.pack()

buttonStop = tk.Button(win, text="Stop", command=Stop)
buttonStop.pack()

buttonabout = tk.Button(win, text="About", command=about)
buttonabout.pack()


win.mainloop()

