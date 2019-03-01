from graphictk import *
# the example inside assignment

Tom=Myturtle()
Tom.left(90)

Tom.color('red')
Tom.move (50)
Tom.left(90)
Tom.move (50)
Tom.left(90)
Tom.move (50)
Tom.left(90)
Tom.move (50)

#test pendown/up
Tom.penup()
Tom.move(200)
Tom.color('blue')
Tom.pendown()
for i in range (4):
    Tom.move (100)
    Tom.right (90)
#second turtle in the screen
Joe=Myturtle()
Joe.color('green')
for i in range (4):
    Joe.move (100)
    Joe.right (90)


