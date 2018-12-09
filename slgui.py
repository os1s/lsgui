import os, webbrowser
from tkinter import *
import threading
import urllib.request
import json

myid = os.environ.get('TwitchClientID')
ls = 'streamlink twitch.tv/_ best'
streamers = ['aphirefly','b0aty','alkaizerx','cutedog_','rigondeaux', 'joniosan','nl_kripp']

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

    def streamer_online(self, streamer):
        content = json.load(urllib.request.urlopen('https://api.twitch.tv/kraken/streams/'+streamer+'?client_id='+myid))
        online = str(content.get('stream'))
        if online == 'None':
            return False
        else:
            return True

    def init_window(self):

        self.master.title(':^)')
        self.pack(fill=BOTH, expand=1)

        yy = 0
        for x in streamers:

            if self.streamer_online(x):
                butt_colour = 'green'
            else:
                butt_colour = 'grey'

            butt = Button(self, text=x, width=10, height=2, bg=butt_colour, command=lambda x=x: self.handle_stream(x))
            butt.place(x=10, y=yy)
            butt = Button(self, text='chat', width=10, height=2, bg=butt_colour, command=lambda x=x: self.open_chat(x))
            butt.place(x=110, y=yy)
            yy += 50

        lab = Label(text="Streamer:")
        lab.place(x=30, y=yy)
        ent = Entry(top)
        ent.bind("<Return>", lambda event: self.handle_stream(ent.get()))
        ent.place(x=100, y=yy, width=80, height=20)


top = Tk()
top.geometry("200x500")
app = Window(top)
top.mainloop()
