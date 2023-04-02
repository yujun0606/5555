# 도형그리기
import turtle as t
t.shape('turtle')
# 정사각형 그리기
def draw_rec():
    for x in range(4):
        t.forward(50)
        t.left(90)

# 정삼각형 그리기
def draw_tri():
    for x in range(3):
        t.forward(50)
        t.left(120)
for x in range(10):
    draw_rec()
    draw_tri()
    t.forward(50)
