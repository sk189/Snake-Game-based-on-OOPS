from turtle import Turtle, pos

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.color("yellowgreen")
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        position = self.segments[len(self.segments)-1].position()
        self.add_segment(position)


    # Making each segment follow its Predecessor, hence ultimately its head, so that the snake can move as a single inter-linked entity
    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
            x_pos = self.segments[segment_number-1].xcor()
            y_pos = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(x_pos, y_pos)  
        self.segments[0].forward(MOVE_DISTANCE)


    # Adding Controls for the snake
    def up(self):
        x = self.head.heading()
        if(x != DOWN):
            self.head.setheading(UP)

    def down(self):
        x = self.head.heading()
        if(x != UP):
            self.head.setheading(DOWN)

    def left(self):
        x = self.head.heading()
        if(x != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        x = self.head.heading()
        if(x != LEFT):
            self.head.setheading(RIGHT)
