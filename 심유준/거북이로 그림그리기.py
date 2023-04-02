# 거북이로 그림 그리기
import turtle as t
def turn_up():
    t.setheading(90)
    t.forward(10)
def turn_down():
    t.setheading(270)
    t.forward(10)
def turn_left():
    t.setheading(180)
    t.forward(10)
def turn_right():
    t.setheading(0)
    t.forward(10)
def ps1():
    t.pensize(10)
def p_up():
    t.up()
    t.color('red')
def p_down():
    t.down()
    t.color('blue')
def blank():
    t.clear()
    
t.shape('turtle')
t.speed(0)
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.onkeypress(ps1, '1')
t.onkeypress(p_up, '4')
t.onkeypress(p_down, '5')
t.onkeypress(blank, '6')
t.listen()
