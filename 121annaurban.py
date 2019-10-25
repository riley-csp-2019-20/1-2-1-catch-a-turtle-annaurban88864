# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "turtle"
turtlesize = 8
turtlecolor = "green"
score = 0
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
tiny = trtl.Turtle(shape=turtleshape)
tiny.color(turtlecolor)
tiny.shapesize(turtlesize)
tiny.speed(0)

score_writer = trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-370, 270)

font_setup = ("Arial", 30, "bold")
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.speed(0)
counter.ht()
counter.penup()
counter.goto(250,275)



#-----game functions--------
def turtle_clicked(x,y):
    print("tiny was clicked")
    change_position()
    score_counter()

def change_position():
    tiny.penup()
    tiny.ht()
    if not timer_up:
      new_xpos = random.randint(-400, 400)
      new_ypos = random.randint(-300, 300)
      tiny.goto(new_xpos, new_ypos)
      tiny.st()

def score_counter():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------

tiny.onclick(turtle_clicked)
wn = trtl.Screen()
wn.bgcolor("gray")
wn.ontimer(countdown, counter_interval)
wn.mainloop()