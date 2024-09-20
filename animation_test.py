import turtle
import time
import random
window = turtle.Screen()
window.bgcolor("white")
window.tracer(0)
ball = turtle.Turtle()
ball.shape("circle")
b_wid = 3
b_len = 3
ball.shapesize(stretch_wid=b_wid,stretch_len=b_len)
acceleration = 0.002
speed = 0.001
colors = ['white', 'black', 'gray', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta',
'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white',
'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'moccasin', 'cornsilk',
'ivory', 'lemon chiffon', 'seashell', 'honeydew', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush',
'misty rose', 'dim gray', 'slate gray', 'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue',
'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue', 'light blue', 'powder blue',
'cadet blue', 'azure', 'light cyan', 'pale turquoise', 'cyan', 'aqua', 'dark turquoise', 'turquoise', 'medium turquoise',
'light sea green', 'dark cyan', 'teal', 'medium aquamarine', 'medium sea green', 'sea green', 'dark sea green',
'aquamarine', 'pale green', 'light green', 'spring green', 'medium spring green', 'dark green', 'green', 'forest green',
'lime green', 'lime', 'lawn green', 'chartreuse', 'green yellow', 'yellow green', 'spring green', 'medium spring green',
'light green', 'pale green', 'dark sea green', 'medium sea green', 'sea green', 'forest green', 'green', 'dark green',
'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod',
'rosy brown', 'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink', 'pale violet red',
'maroon', 'medium violet red', 'violet red', 'magenta', 'violet', 'plum', 'orchid', 'medium orchid', 'dark orchid',
'dark violet', 'blue violet', 'purple', 'medium purple', 'thistle', 'snow', 'white', 'white smoke', 'gainsboro',
'light grey', 'silver', 'dark grey', 'grey', 'dim grey', 'black'
]
shapes = ["triangle","turtle","square","circle"]
def transition_into_color(color,ball,b_len,b_wid,acceleration,speed,window,shape):
    ball.color(color)
    ball.shape(shape)
    ball.showturtle()
    for i in range(270):
        ball.left(speed * 5)
        b_len += speed
        b_wid += speed
        speed += acceleration
        time.sleep(0.01)
        ball.shapesize(stretch_wid=b_wid,stretch_len=b_len)
        window.update()
    ball.hideturtle()
    b_len = 3
    b_wid = 3
    window.bgcolor(color)
    speed = 0.001
while True:
    transition_into_color(random.choice(colors),ball,b_len,b_wid,acceleration,speed,window,random.choice(shapes))


    
    
