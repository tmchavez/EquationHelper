from tkinter import *

root = Tk()

theFrame = Frame(root)
theFrame.pack()

curwidth = 1000
curheight = 900

w = Canvas(root, width = curwidth, height = curheight)
w.pack()

def draw_grid(ch,cw,lineSize,space):
    a = int((cw/100)*2)
    b = int((ch/100)*2)
    print (a)
    print (b)

    counter = 1
    for x in range(a):
        if (counter%2) != 0 :
            w.create_line(counter*space,0,counter*space,ch,fill="blue",width=lineSize/2)
        else:
            w.create_line(counter*space,0,counter*space,ch,fill="blue",width=lineSize)
        counter += 1

    counter = 1
    for x in range(b):
        if (counter%2) != 0 :
            w.create_line(0, counter*space,cw, counter*space,fill="blue",width=lineSize/2)
        else:
            w.create_line(0, counter*space,cw, counter*space,fill="blue",width=lineSize)
        counter += 1


def draw_x(brX,brY,name,size):
    half = size/2
    offset = size/8
    points = (brX,brY,
              brX-(half-offset),brY-half,
              brX,brY-size,
              brX-offset ,brY-size,
              brX-half,brY-(half+offset),
              brX-(size-offset),brY-size,
              brX-size,brY-size,
              brX-(half+offset),brY-half,
              brX-size,brY,
              brX-(size-offset),brY,
              brX-half,brY-(half-offset),
              brX-offset,brY
              )
    name = w.create_polygon(points)



draw_grid(curheight,curwidth,4.0,50)
draw_x(200,200,"lol",150)

for x in range(5):
  draw_x(400,x*100, "meme",50)

root.mainloop()
