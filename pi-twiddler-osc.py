import tkinter as tk
import sys
from pythonosc import udp_client

def func(e=None):
    client.send_message("/pi0", e.char)

def funcExit(e=None):
    sys.exit()
    
client = udp_client.SimpleUDPClient("10.0.0.10",8888)
main=tk.Tk()
main.bind('<KeyPress>',func)
main.bind('<Escape>',funcExit)
main.attributes("-fullscreen", True)
main.configure(background='black')
main.mainloop()
