import os, webbrowser
from tkinter import *
import threading

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def handle_stream(self, streamer):
        def openstream():
            os.system('C:\\Users\\scrsm\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\livestreamer.exe twitch.tv/'+streamer+' best')
        t = threading.Thread(target=openstream)
        t.start()

    def open_chat(self, streamer):
        webbrowser.open('https://www.twitch.tv/popout/'+streamer+'/chat')

    def init_window(self):

        self.master.title(':^)')
        self.pack(fill=BOTH, expand=1)

        butt = Button(self, text='alkaizerX', width=12, height=2, command=lambda: self.handle_stream('alkaizerx'))
        butt.place(x=100, y=0)

        butt = Button(self, text='chat', width=12, height=2, command=lambda: self.open_chat('alkaizerx'))
        butt.place(x=200, y=0)

        butt = Button(self, text='b0aty', width=12, height=2, command=lambda: self.handle_stream('b0aty'))
        butt.place(x=100, y=50)

        butt = Button(self, text='chat', width=12, height=2, command=lambda: self.open_chat('b0aty'))
        butt.place(x=200, y=50)

        butt = Button(self, text='joniosan', width=12, height=2, command=lambda: self.handle_stream('joniosan'))
        butt.place(x=100, y=100)

        butt = Button(self, text='chat', width=12, height=2, command=lambda: self.open_chat('joniosan'))
        butt.place(x=200, y=100)

top = Tk()
top.geometry("400x300")
app = Window(top)
top.mainloop()
