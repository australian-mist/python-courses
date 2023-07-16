import turtle as t

t.speed(7)
t.color('brown3')
t.width(3)

t.penup()
t.goto(-100, -100)
t.pendown()

i = 5
dist = 150
angle = 360/i

while i > 0:
    t.left(angle)
    t.forward(dist)
    i -= 1

t.penup()
t.forward(200)
t.pendown()
t.circle(100)


t.clear()
t.penup()
t.home()
t.pendown()


i = 5
dist = 70

while i > 0:
    j = 0
    while j < 4:
        t.left(90)
        t.forward(dist*4)
        j += 1
    t.right(angle)
    t.circle(dist)
    i -= 1


t.clear()
t.penup()
t.home()
t.pendown()


t.bgcolor('#DEB887')

colors = ['#40E0D0', '#AFEEEE', '#008080', '#8FBC8F', '#7FFFD4', '#5F9EA0']
n = 6
angle = 360 / n - 1

for i in range(151):
    t.pencolor(colors[i % n])
    t.width(i // 50 + 1)
    t.left(angle)
    t.forward(i)


t.mainloop()
