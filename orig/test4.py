import tkinter as tk
import sys

def func(event=None):
    tk.Label(main, text="mew").pack()

def funcExit(event=None):
    sys.exit()
    
main=tk.Tk()
main.bind('<Return>',func)
main.bind('<Escape>',funcExit)
main.configure(background='black')
main.mainloop()
