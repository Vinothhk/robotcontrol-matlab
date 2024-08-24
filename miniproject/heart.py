import sys
import tkinter as tk
from tkinter import messagebox


def disp():
    msg = tk.Label(window,text=f'\U0001F617 Yes I am Loving Youu',anchor='center').pack()
    
def word():
    t = entry.get()
    tk.Label(window,text=f'Love you {t} \u2764\ufe0f!',anchor='center').pack()
    #print(f'Love you {t}')
    
def handler(event):
    word()

def percent(event):
    p = v.get()
    per = tk.Label(window,text=f'\u2764\ufe0f Love you {p:.0f} % \u2764\ufe0f',anchor='center')
    per.pack()
h=3
print("\u2764\ufe0f")
window = tk.Tk()
window.title("LOVE MACHINE")
window.geometry("700x700")

v= tk.DoubleVar()
tk.Label(window,text='Hi').pack()
tk.Button(window,text='Love?',command=disp,height=h,width=h,anchor='center').pack()
entry = tk.Entry(window,textvariable='H')
entry.pack()

s = tk.Scale(window, variable = v,from_ = 1, to = 100, orient =tk.HORIZONTAL,command=percent,length=500)
s.pack()  

window.bind('<Return>',handler)
tk.Button(window,text='Go!',command=word,anchor='center').pack()

window.mainloop()
