import tkinter as tk
import sys

def func(e=None):
    tk.Label(main, text="mew " + e.char).pack()

def funcExit(e=None):
    sys.exit()
    
main=tk.Tk()
main.bind('<KeyPress>',func)
main.bind('<Escape>',funcExit)
main.configure(background='black')
main.mainloop()
