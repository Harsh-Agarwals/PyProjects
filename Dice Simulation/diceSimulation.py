import numpy as np
import turtle

# -------------------SIMULATION DESIGN-1-----------------------
# def graphics(num):
#     for i in range(num):
#         for j in range(4):
#             turtle.forward(100)
#             turtle.right(90)
#         deg = 360/num
#         turtle.right(deg)
#     turtle.done()

# ---------------------CIRCULAR RING DESIGN FOR SIMULATION----------------------
def ring(col, rad):
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

# -----------------------SIMULATION DESIGN-2-------------------------
def graphics(number):
    for i in range(number):
        turtle.up()
        turtle.forward(70)
        turtle.down()
        ring('black', 30)
        turtle.up()
        turtle.setpos(0, 0)
        turtle.down()
        deg = 360/number
        turtle.right(deg)
    turtle.done()


def game_continue():
    return input("Do you want to continue?? [Y/N]")


def game_on():
    cont = game_continue().lower()
    if cont in ['yes', 'y']:
        import turtle
        return True
    elif cont in ['no', 'n']:
        return False
    else:
        print("Input not understood... try again")
        game_on()


while True:
    num = np.random.randint(1, 7)
    print(num)
    graphics(num)
    if game_on():
        continue
    else:
        break
