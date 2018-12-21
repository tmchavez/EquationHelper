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

def draw_y(brX,brY,name,size):
    half = size/2
    offset = size/8
    points = (brX,brY-(size-offset),
              brX-offset,brY-size,
              brX-half,brY-(half+offset),
              brX-(size-offset),brY-size,
              brX-size,brY-(size-offset),
              brX-(half+offset),brY-half,
              brX-size,brY-offset,
              brX-(size-offset),brY
              )

    name = w.create_polygon(points)

def draw_rect(brX,brY,name,size):
    points = (brX,brY,
              brX-size,brY,
              brX-size,brY-(size/4),
              brX,brY-(size/4)
    )
    name = w.create_polygon(points)


def draw_equal(brX,brY,name,size):
    half = size/2
    offset = size/8
    name1 = name + "a"
    name2 = name + "b"
    draw_rect(brX-(size/5),brY-(half/2),name1,size-(half-offset))
    draw_rect(brX-(size/5),brY-(size*(2/3)),name2,size-(half-offset))

def draw_minus(brX,brY,name,size):
    half = size/2
    offset = size/8
    draw_rect(brX-offset,brY-(half-(offset/2)),name,size-(2*offset))

def draw_rectV(brX,brY,name,size):
    points = (brX,brY,
              brX-(size/4),brY,
              brX-(size/4),brY-size,
              brX,brY-size
    )
    name = w.create_polygon(points)

def draw_1(brX,brY,name,size):
    half = size/2
    offset = size/8
    draw_rectV((brX-half)+offset,brY,name,size)

draw_grid(curheight,curwidth,4.0,50)
draw_x(200,200,"lol",100)
draw_equal(300,200,"eq",100)
draw_y(400,200,"aName",100)
draw_minus(500,200,"minu",100)
draw_1(600,200,"uno",100)


root.mainloop()
