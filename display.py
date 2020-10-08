#by Nathaniel Imel

import nltk
import process_content as pc
from tkinter import Tk, Canvas, Frame, BOTH, W

class Display(Frame):
    pasts = pc.tenselist[0]
    presents = pc.tenselist[1]
    others = pc.tenselist[2]

    def __init__(self):
        super().__init__()

        #get tense sentences
        self.initUI()

    def initUI(self):

        self.master.title("Timeline")
        self.pack(fill=BOTH, expand=1)

        #main timeline
        canvas = Canvas(self)
        canvas.create_line(50, 180, 950, 180)

        #labels
        canvas.create_line(500, 160, 500, 200)
        canvas.create_text(490, 150, anchor=W, font="Purisa",
            text="Now")
        canvas.create_line(800, 160, 800, 200)
        canvas.create_text(780, 150, anchor=W, font="Purisa",
            text="Future or Irrealis")
        canvas.create_line(200, 160, 200, 200)
        canvas.create_text(190, 150, anchor=W, font="Purisa",
            text="Past")

        #Display events
        count = 0
        for e in self.pasts:
            canvas.create_text(100, 210 + count, anchor=W, font="Purisa",
                text= e)
            count += 20

        count = 0
        for e in self.presents:
            canvas.create_text(480, 210 + count, anchor=W, font="Purisa",
                text= e)
            count += 20

        count = 0
        for e in self.others:
            canvas.create_text(800, 210 + count, anchor=W, font="Purisa",
                text= e)
            count += 20

        canvas.pack(fill=BOTH, expand=1)

def __main__():
    root = Tk()
    d = Display()
    root.geometry("1200x500")
    root.mainloop()
