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

    def joniosan(self):
        os.system('C:\\Users\\scrsm\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\livestreamer.exe twitch.tv/joniosan best')

    def alkchat(self):
        webbrowser.open('https://www.twitch.tv/popout/alkaizerx/chat')

    def b0atychat(self):
        webbrowser.open('https://www.twitch.tv/popout/b0aty/chat')

    def jonichat(self):
        webbrowser.open('https://www.twitch.tv/popout/joniosan/chat')

    def init_window(self):

        self.master.title(':^)')
        self.pack(fill=BOTH, expand=1)

        butt = Button(self, text='alkaizerX', width=12, height=2, command=self.alkaizerx)
        butt.place(x=100, y=0)

        butt = Button(self, text='chat', width=12, height=2, command=self.alkchat)
        butt.place(x=200, y=0)

        butt = Button(self, text='b0aty', width=12, height=2, command=self.b0aty)
        butt.place(x=100, y=50)

        butt = Button(self, text='chat', width=12, height=2, command=self.b0atychat)
        butt.place(x=200, y=50)

        butt = Button(self, text='joniosan', width=12, height=2, command=self.joniosan)
        butt.place(x=100, y=100)

        butt = Button(self, text='chat', width=12, height=2, command=self.jonichat)
        butt.place(x=200, y=100)



top = Tk()
top.geometry("400x300")
app = Window(top)
top.mainloop()
