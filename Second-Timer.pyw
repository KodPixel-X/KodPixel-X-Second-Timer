import tkinter
from tkinter import messagebox

win = Tkinter.Tk()
win.title("Second-Timer")
win.geometry("500x550")
win.config(bg="red")

messagebox.info("Second-Timer", "This is a Second Timer.")

def plus():
    while(true):
        
    text=str(int(plus.config.Label.cget("text")) + 1)
    plus.config.Label.after(1000, plus)
    


label = tkinter.Label(win, text="0" font=("Arial", 25)
label.pack()

button = tkinter.buton(win, text="START", command=plus)
button.pack()

win.mainloop()
