from turtle import Turtle, Screen

#BAR = Turtle(shape = "square")  #default square size = 20×20  BARとした方がいいのかself.barとした方がいいの
GAME_IS_ON = True
X = -260
Y = -260
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Bar:
    
    def __init__(self):
        self.new_bar = []
        self.bar = Turtle(shape = "square")
        self.create_bar()   #ここでcreate_bar()を呼んでいるので、main.pyの方でcreate_bar()を呼ばなくて良い！

    def create_bar(self):
        self.bar.penup()
        self.bar.setpos(X,Y)
        self.bar.color("white","white")
        for i in range(0,3):
            self.new_bar.append(i)
            length = len(self.new_bar)
        #print(length)
        self.bar.turtlesize(stretch_wid=1,stretch_len=length,outline=1)  #barの大きさ長くする
    
    def move(self):
        self.bar.penup()
        for i in range(100):   #while game_is_on:
            self.bar.forward(20)
            #if self.bar.head.distance(self.bar) < 15:
            #    print("Food Detection!!")

    def up(self):
        self.bar.setheading(UP)

    def down(self):
        self.bar.setheading(DOWN)

    def right(self):
        self.bar.setheading(RIGHT)

    def left(self):
        self.bar.setheading(LEFT)
    
    def home(self):     #まだ使用していない
        GAME_IS_ON = False
        self.bar.home()
