import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Second-Timer")
win.geometry("520x570")
win.config(bg="red")

messagebox.showinfo("Second-Timer", "This is a Second Timer.")

label = tk.Label(win, text="0", font=("Arial", 25))
label.pack(pady=20)

def plus():
    current = int(label.cget("text"))
    label.config(text=str(current + 1))
    win.after(1000, plus)

def blue():
    win.config(bg="blue")

def red():
    win.config(bg="red")

def green():
    win.config(bg="green")

    

button = tk.Button(win, text="START", command=plus)
button.pack(pady=10)

buttonb = tk.Button(win, text="Make the background color blue.", command=blue)
buttonb.pack()

buttonr = tk.Button(win, text="Make the background color red.", command=red)
buttonr.pack()

buttong = tk.Button(win, text="Make the background color blue.", command=green)
buttong.pack()


win.mainloop()

