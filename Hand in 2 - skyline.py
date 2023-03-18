import turtle as t
import random

canvas_width = 500
canvas_height = 500
canvas_width_range = range(501)

t.setworldcoordinates(0, 0, canvas_width, canvas_height)
t.bgcolor("black")


# Drawing from back to front, I want to place random stars, that are covered up by the buildings, in case they are in the
# same place, therefore I start with the stars.

def turtle_move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def stars():
    t.fillcolor("white")
    for x in range(25):
        t.speed(100)
        x_position = random.randint(0, 500)
        y_position = random.randint(150, 500)
        turtle_move(x_position, y_position)
        t.begin_fill()
        t.circle(2)
        t.end_fill()

class Highrise:
    def __init__(self, color="grey", start_coordinate=-60, build_width=random.randint(50,140), build_height=random.randint(180, 485)):
        self.start_coordinate=start_coordinate
        self.color=color;
        self.width=build_width;
        self.height=build_height;
        self.build_x=start_coordinate+build_width
    def draw_building(self, build_y=-10):
        t.fillcolor(self.color)
        turtle_move(self.build_x, build_y)
        t.begin_fill()
        t.begin_poly()
        t.setheading(180)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.end_poly()
        t.end_fill()
        t.penup()
        windows(self.start_coordinate, self.build_x, 0, self.height)

        #self.build_x += self.width

    def get_build_x(self):
        return self.build_x;

def highrise2():
    last_build_x = -60
    for j in range(6):
        high_rise = Highrise(start_coordinate=last_build_x, build_width=random.randint(50,140), build_height=random.randint(180, 485));
        high_rise.draw_building();
        last_build_x = high_rise.get_build_x()
        #total_poly[j].append(t.get_poly())


def highrise():
    global high_poly_1, high_poly_2, high_poly_3, high_poly_4, high_poly_5, high_poly_6, total_poly
    high_poly_1 = []            #Trying to create some definitions of where the buildings actually
    high_poly_2 = []            # end up so i maybe can use it later, how i dont know
    high_poly_3 = []            # But my intentions has been stated futher down
    high_poly_4 = []
    high_poly_5 = []
    high_poly_6 = []
    total_poly = [high_poly_1, high_poly_2, high_poly_3, high_poly_4, high_poly_5, high_poly_6]

    last_build_x = -60

    for j in range(6):
        t.fillcolor("grey")
        build_width = random.randint(50, 140)
        build_height = random.randint(180, 485)
        build_x = last_build_x + build_width + random.randint(40, 60)
        build_y = -10

        turtle_move(build_x, build_y);

        t.begin_fill()
        t.begin_poly()
        t.setheading(180)
        t.forward(build_width)
        t.right(90)
        t.forward(build_height)
        t.right(90)
        t.forward(build_width)
        t.right(90)
        t.forward(build_height)
        t.end_poly()
        t.end_fill()
        t.penup()

        last_build_x += build_width

        total_poly[j].append(t.get_poly())
        windows(last_build_x, build_x, 0, build_height)

def windows(total_poly_x_min=3,total_poly_x_max=30,total_poly_y_min=3,total_poly_y_max=30):
    t.fillcolor("white")
    # Draw squares randomly
    for i in range(10):                                             #Example window amount
        x = random.randint(total_poly_x_min+2, total_poly_x_max-2)      #Example explanitory text
        y = random.randint(total_poly_y_min, total_poly_y_max)      # I know that this is invalid but its to point out where i want my windows to be
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(4):
            t.forward(10)
            t.right(90)
        t.end_fill()



stars()
highrise2()
#windows()
t.mainloop()