import turtle
import time
import random
from pygame import mixer

delay = 0.1
score = 0
high_score = 0


screen = turtle.Screen()
screen.title("                                                                           Ali Salimi Snake Game")
screen.bgcolor("lightblue")

screen.setup(width=600, height=600)
screen.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "up"


food = turtle.Turtle()
colors = random.choice(['green', 'purple', 'yellow'])
shapes = 'circle'
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

write = turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("white")
write.penup()
write.ht()
write.goto(0, 250)
write.write("امتیاز : 0 بالاترین امتیاز : 0 ", align="center",
            font=("B Koodak", 24, "bold"))


def up():
    if snake.direction != "down":
        snake.direction = "up"


def down():
    if snake.direction != "up":
        snake.direction = "down"


def left():
    if snake.direction != "right":
        snake.direction = "left"


def right():
    if snake.direction != "left":
        snake.direction = "right"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

m = []


while True:
    screen.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "up"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in m:
            segment.goto(1000, 1000)
        m.clear()
        score = 0
        delay = 0.1
        write.clear()
        write.write("بازی تمام شد".format(
            score, high_score), align="center", font=("B Koodak", 24, "bold"))
        time.sleep(1)
        write.clear()
        write.write("امتیاز = {} بالاترین امتیاز = {} ".format(
            score, high_score), align="center", font=("B Koodak", 24, "bold"))
    if snake.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")  # tail color
        new_segment.penup()
        m.append(new_segment)
        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        write.clear()
        write.write("امتیاز = {} بالاترین امتیاز = {} ".format(
            score, high_score), align="center", font=("B Koodak", 24, "bold"))

    for index in range(len(m) - 1, 0, -1):
        x = m[index - 1].xcor()
        y = m[index - 1].ycor()
        m[index].goto(x, y)
    if len(m) > 0:
        x = snake.xcor()
        y = snake.ycor()
        m[0].goto(x, y)
    move()
    for segment in m:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "up"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for s in m:
                s.goto(1000, 1000)
            m.clear()

            score = 0
            delay = 0.1
            write.clear()
            write.write("بازی تمام شد".format(
                score, high_score), align="center", font=("B Koodak", 24, "bold"))
            time.sleep(1)
            write.clear()
            write.write("امتیاز = {} بالاترین امتیاز = {} ".format(
                score, high_score), align="center", font=("B Koodak", 24, "bold"))
    time.sleep(delay)