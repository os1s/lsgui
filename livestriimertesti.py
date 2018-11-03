import os, webbrowser
from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def alkaizerx(self):
        os.system('C:\\Users\\scrsm\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\livestreamer.exe twitch.tv/alkaizerx best')

    def b0aty(self):
        os.system('C:\\Users\\scrsm\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\livestreamer.exe twitch.tv/b0aty best')

    def alkchat(self):
        webbrowser.open('https://www.twitch.tv/popout/alkaizerx/chat')

    def init_window(self):

        self.master.title(':^)')
        self.pack(fill=BOTH, expand=1)

        butt = Button(self, text='alkaizerX', width=12, height=2, command=self.alkaizerx)
        butt.place(x=150, y=0)

        butt = Button(self, text='chat', width=12, height=2, command=self.alkchat)
        butt.place(x=250, y=0)

        butt = Button(self, text='b0aty', width=12, height=2, command=self.b0aty)
        butt.place(x=150, y=50)

top = Tk()
top.geometry("400x300")
app = Window(top)
top.mainloop()
