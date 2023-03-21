import turtle as t
import random

canvas_width = 500
canvas_height = 500

t.setup(canvas_width + 20, canvas_height + 20)
t.setworldcoordinates(-10, -10, canvas_width + 10, canvas_height + 10)

t.bgcolor("black")

# Drawing from back to front, I want to place random stars, that are covered up by the buildings, in case they are in the
# same place, therefore I start with the stars.

def stars():
    t.fillcolor("white")
    for x in range(25):
        t.speed(100)
        x_position = random.randint(0, 500)
        y_position = random.randint(150, 500)
        t.penup()
        t.goto(x_position, y_position)
        t.pendown()
        t.begin_fill()
        t.circle(2)
        t.end_fill()
stars()

class skyline:
    def __init__(self, color="grey", build_width=random.randint(40, 90), build_height=random.randint(80, 185),
    start_coordinate=(-10, -10), total_width=0, extra_height=random.randint(40, 100), total_height=0, skyline_shape =[]):
        self.color = color
        self.width = int(build_width)
        self.height = int(build_height)
        self.start = start_coordinate
        self.total_width = total_width
        self.total_height = total_height
        self.taller_building = extra_height
        self.skyline_shape = skyline_shape
        self.x_coordinates = [0, 500]
        self.y_coordinates = [0]
    def info(self):
        self.total_height += self.height
        self.total_width += self.width
        self.x_coordinates.append(int(t.xcor()))
        self.y_coordinates.append(int(t.ycor()))
    def upwards(self):
        t.setheading(90)
        t.forward(self.height)
        t.setheading(0)
        t.forward(self.width)
        self.info()
    def extra_height(self):
        t.setheading(90)
        t.forward(self.taller_building)
        t.setheading(0)
        t.forward(self.width)
        self.info()
    def downwards(self):
        t.setheading(270)
        t.forward(self.taller_building + random.randint(30, 80))
        self.total_height -= self.height
        self.x_coordinates.append(int(t.xcor()))
        self.y_coordinates.append(int(t.ycor()))
    def down_long(self):
        t.setheading(270)
        t.goto(t.xcor(), 120)
        self.total_height = 120
        self.x_coordinates.append(int(t.xcor()))
        self.y_coordinates.append(int(t.ycor()))
    def sideways(self):
        t.setheading(0)
        t.forward(self.width)
        self.info()
    def draw_skyline(self):
        t.fillcolor(self.color)
        t.penup()
        t.goto(self.start)
        t.begin_fill()
        t.begin_poly()
        while self.total_width < canvas_width -100:
            if self.total_width >= 500:
                break
            t.setheading(90)
            t.forward(100)
            self.sideways()
            self.upwards()
            self.extra_height()
            self.down_long()
            self.extra_height()
            self.down_long()
            if self.total_height >= 400:
                self.down_long()
            if self.total_width >= canvas_width:
                break
        t.setheading(270)
        t.goto(t.xcor(), -10)
        t.end_fill()
        t.end_poly()
        self.skyline_shape = t.get_poly()

skyline_instance = skyline()
skyline_shape = skyline_instance.skyline_shape

class windows:
    def __init__(self, square_size=10, color="White", skyline_x_cor=skyline_instance.x_coordinates,
                 skyline_y_cor=skyline_instance.y_coordinates):
        self.color = color
        self.square_size = square_size
        self.sky_x = (skyline_x_cor)
        self.sky_y = (skyline_y_cor)
        self.x_coordinate = random.randint(self.sky_x[0], self.sky_x[-1])
        self.y_coordinate = random.randint(self.sky_y[0], self.sky_y[-1])
        self.overlaps = False
        for shape_place in skyline_shape:
            if (shape_place[0] < self.x_coordinate + self.square_size and shape_place[2] > self.x_coordinate
            and shape_place[1] < self.y_coordinate + self.square_size and shape_place[3] > self.y_coordinate):
                self.overlaps = True
            break
    def plotting_windows(self):
        t.penup()
        t.goto(self.x_coordinate, self.y_coordinate)
        t.setheading(0)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        for i in range(4):
            t.forward(self.square_size)
            t.right(90)
        t.end_fill()

skyline_instance.draw_skyline()
skyline_instance = skyline()
for j in range(15):
    windows_instance = windows()
    windows_instance.plotting_windows()
t.mainloop()
