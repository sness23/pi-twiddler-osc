import tkinter as tk
import sys

class FullScreenApp(object):
    def close(event):
        self.master.destroy
    def __init__(self, master, **kwargs):
        self.master=master
        master.configure(background='black')
        master.attributes("-fullscreen", True)
        master.bind('<Escape>', self.close)
        
root = tk.Tk()
app=FullScreenApp(root)
root.mainloop()




