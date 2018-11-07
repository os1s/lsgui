import os, webbrowser
from tkinter import *
import threading

ls = 'C:\\Users\\scrsm\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\livestreamer.exe twitch.tv/_ best'
streamers = ['alkaizerx','b0aty','joniosan','cutedog_','rigondeaux','rexitus']

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def handle_stream(self, streamer):
        def openstream():
            os.system(ls.replace('_', streamer))
        t = threading.Thread(target=openstream)
        t.start()

    def open_chat(self, streamer):
        webbrowser.open('https://www.twitch.tv/popout/'+streamer+'/chat')

    def init_window(self):

        self.master.title(':^)')
        self.pack(fill=BOTH, expand=1)

        yy = 0
        for x in streamers:
            butt = Button(self, text=x, width=12, height=2, command=lambda x=x: self.handle_stream(x))
            butt.place(x=100, y=yy)
            butt = Button(self, text='chat', width=12, height=2, command=lambda x=x: self.open_chat(x))
            butt.place(x=200, y=yy)
            yy += 50

top = Tk()
top.geometry("400x300")
app = Window(top)
top.mainloop()
