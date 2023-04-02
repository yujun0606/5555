# 함수로 다각형 그리기
import turtle as t
def move_t(x, y):
    t.up()
    t.goto(x, y)
    t.down()
def draw(a, b, x, y):
    move_t(x, y)
    for x in range(a):
        t.forward(b)
        t.left(360/a)
draw(5, 50, 150, 150)
draw(6, 70, 150, -150)
draw(7, 90, -150, -150)
draw(8, 110, -150, 150)
draw(10, 50, 0, 0)
