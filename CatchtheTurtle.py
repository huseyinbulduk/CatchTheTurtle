import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ('Arial', 30, 'normal')
score = 0
game_over = False

#turtle_list
turtle_list = []

#score_turtle

score_turtle = turtle.Turtle()

#countdown_turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()  #turtle'ı gizlemek
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height()
    y = top_height * 0.45
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

grid_size = 15
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)

    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10,-20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles(): #turtle'ları gizlemek
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly(): #rastgele turtle'lardan birini çağırmak
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()  # turtle'ı gizlemek
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    top_height = screen.window_height()
    y = top_height * 0.40
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


turtle.tracer(0) #turtle animasyonunu sıfırlar.
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtle_randomly()
countdown(10)
turtle.tracer(1)
turtle.mainloop()