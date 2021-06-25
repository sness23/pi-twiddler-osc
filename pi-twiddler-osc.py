import tkinter as tk
import sys
from pythonosc import udp_client
import syslog
outStr = ""
client = udp_client.SimpleUDPClient("10.0.0.10",8888)
main=tk.Tk()
text = tk.StringVar()
text.set("(^_^)")
label = tk.Label(main, textvariable=text, font=("Helvetica", 50)).pack()

def funcAdd(e=None):
    global outStr
    outStr += e.char

def funcClear(e=None):
    global outStr
    outStr = ""

def funcSend(e=None):
    text.set(outStr)
    print(outStr)
    syslog.syslog(outStr)
    client.send_message("/pi0", outStr)

def funcExit(e=None):
    sys.exit()

main.bind('a',funcClear)
main.bind('b',funcSend)
main.bind('0',funcAdd)
main.bind('1',funcAdd)
main.bind('2',funcAdd)
main.bind('4',funcAdd)
main.bind('<Escape>',funcExit)
main.attributes("-fullscreen", True)
main.configure(background='black')
main.mainloop()
