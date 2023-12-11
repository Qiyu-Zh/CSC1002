from turtle import Turtle,Screen
import turtle
from functools import partial
import time
import random
KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,SPACE = 'Up','Down','Left','Right','space'
list_snake=[]
list_snake_pos=[]
g_snake =None
g_monster=None
g_screen=None
overlap=False
t0,t1,t2,t3,t4,t5,t6,t7,t8,t9=None,None,None,None,None,None,None,None,None,None
listTurtle=[t1,t2,t3,t4,t5,t6,t7,t8,t9]
direction='right'
extend_length=5
state_running=True
contracting_times=0
startTime=None
speed_snake=0
listFood=[]


def origin_of_monster():
    while True:
        a=random.randint(-235,235)
        b=random.randint(-235,235)
        if distance((a,b),(0,0))>90:
            return (a,b)
      
def configureScreen(w=500,h=500):
    s=Screen()
    s.setup(w,h)
    s.title('Snake by Zhang Qiyu')
    s.tracer(0)
    return s

def configureTurtle(shape='square',color='red',x=0,y=0):
    t=Turtle(shape)
    t.up()
    t.color(color)
    t.goto(x,y)
    return t

def contacted():
    global list_snake_pos
    pos2=g_monster.position()
    for i in list_snake_pos:
        if distance((i[0],i[1]),pos2)<15:
            return True
    return False

def moveUp():
    global direction
    direction='up'
    g_snake.setheading(90)

def moveDown():
    global direction
    direction='down'
    g_snake.setheading(270)

def moveLeft():
    global direction
    direction='left'
    g_snake.setheading(180)
    
def moveRight():
    global direction
    direction='right'
    g_snake.setheading(0)
def movesnake(d=20):
    global extend_length,contracting_times,startTime,speed_snake
    speed_snake=270
    if state_running==True:
        if contacted():
            contracting_times+=1
        if distance(g_snake.position(),g_monster.position())<15:
            fail()
            return 
        if listFood==[]: 
            win()
            return  
        if checkBoundary():
            if check_eat_food() == False and extend_length==0:
                    extend_no_eating()
            else:
                extend_eating()
                extend_length-=1
                speed_snake=350
            g_snake.forward(d)
        g_screen.title('Snake: Contracted: %d, Time: %d' %(contracting_times, int(time.time() - startTime)))
        g_screen.update()
    g_screen.ontimer(movesnake,speed_snake)

def movemonster(d=20):
    global speed_snake
    if distance(g_snake.position(),g_monster.position())<15 or listFood==[]:
        return
    speed_monster=random.randint(speed_snake-10,speed_snake+100)
    pos=g_snake.position()
    pos2=g_monster.position()
    if abs(pos[0]-pos2[0])>abs(pos[1]-pos2[1]):
        if pos[0]>pos2[0]:
            g_monster.setheading(0)
        else:
            g_monster.setheading(180)
    else:
        if pos[1]>pos2[1]:
            g_monster.setheading(90)
        else:
            g_monster.setheading(270)
    g_monster.forward(d)
    g_screen.update()
    g_screen.ontimer(movemonster,speed_monster)

def checkBoundary():
    pos=g_snake.position()
    if (pos[0]>230 and direction=='right') or (pos[0]<-230 and direction=='left') or (pos[1]>230 and direction=='up') or (pos[1]<-230 and direction=='down'):
        return False
    return True

def fail():
    g_snake.write('Game Over!!', align='right', font='Arial 16 bold')
    return 

def win():
    g_snake.write('Congratulations,you win!!', align='right', font='Arial 16 bold')
    return


def pause():
    global state_running
    state_running=not state_running

def configureKey(s):
    s.onkey(moveUp,KEY_UP)
    s.onkey(moveDown,KEY_DOWN)
    s.onkey(moveLeft,KEY_LEFT)
    s.onkey(moveRight,KEY_RIGHT)
    g_screen.onkey(pause,SPACE)
    s.listen()

def extend_no_eating(heading=0,dist=20):
    list_snake_pos.append(g_snake.position())
    color=g_snake.color()
    g_snake.color('red','orange')
    a=g_snake.stamp()
    list_snake.append(a)  
    g_snake.clearstamp(list_snake[0])
    del list_snake[0]
    del list_snake_pos[0]
    g_snake.color(*color)
    g_screen.update()

def extend_eating():
    list_snake_pos.append(g_snake.position())
    color=g_snake.color()
    g_snake.color('red','orange')
    a=g_snake.stamp()
    list_snake.append(a)  
    g_snake.color(*color)
    g_screen.update()
  
def check_eat_food():
    global extend_length
    pos=g_snake.position()

    for i in listFood:
        if distance((i[0],i[1]),pos)<15:
            listFood.remove(i)
            listTurtle[i[2]-1].clear()
            extend_length+=i[2]
            return True
    return False

def distance(a,b):
    return  ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5  
def write():
    global t0
    t0=turtle.Turtle()
    t0.penup()
    t0.setposition(-200,50)
    t0.pendown()
    t0.write('''Welcome to my version of snake...
You are going to use the 
4 arrow keys to move the snake
around the screen, trying to 
consume all the food items
before the monster catches you...

Click anywhere on the screen 
to start the game, good luck to you''',font='aerial 15 bold')
    t0.hideturtle()
def setfood():
    global listTurtle
    i=1
    while True:
        valid=True
        a=random.randint(-235,235)
        b=random.randint(-235,235)
        for j in listFood:
            if distance((j[0],j[1]),(a,b))<60 and distance((a,b),(0,0))<15:
                valid=False
        if valid == True:
            listTurtle[i-1]=turtle.Turtle()
            listFood.append([a,b,i])
            listTurtle[i-1].penup()
            listTurtle[i-1].setposition(a,b)
            listTurtle[i-1].pendown()
            listTurtle[i-1].write(str(i),font='aerial 10 bold')
            listTurtle[i-1].hideturtle() 
            i+=1
        if i==10:
            break

    
def start(a,b):
    global startTime,listTurtle
    startTime=time.time()  
    t0.clear()
    setfood()
    g_screen.onclick(None)
    g_screen.update()
    movesnake()
    movemonster() 
    configureKey(g_screen)

if __name__ =='__main__':
    g_screen=configureScreen()
    g_snake = configureTurtle()
    monster=origin_of_monster()
    g_monster = configureTurtle(color='purple',x=monster[0],y=monster[1])
    write()   
    g_screen.update()
    g_screen.onclick(start)
    g_screen.mainloop()
