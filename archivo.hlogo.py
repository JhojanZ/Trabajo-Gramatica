import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.title('Logo Interpreter')

def VAR():
    delta = 0
    for _ in range(20):
        t.forward(100 + delta)
        t.right(90)
        if delta % 100 == 0:
            t.width(delta / 100)
        delta = (delta + 50)

def main():
    VAR()


main()
turtle.done()
