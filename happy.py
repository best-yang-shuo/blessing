#1.导入
import random
from math import *
import turtle
import time
from turtle import mainloop, hideturtle

#2.生成斐波契那数列
def FRt(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return FRt(n-1)+FRt(n-2)
def FR(n):
    result_list=[]
    for i in range(1,n+3):
        result_list.append(FRt(i))
    return result_list

#3.定义生成叶子方法
def leaf(x,y,node):
    til=turtle.heading()
    i=random.random()
    an=random.randint(10,180)
    ye=random.randint(6,9)
    ye=ye/10
    turtle.color(ye,ye*0.9,0)
    turtle.fillcolor(ye+0.1,ye+0.05,0)
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(an+90)
    turtle.forward(8*i)
    px=turtle.xcor()
    py=turtle.ycor()
    turtle.begin_fill()
    turtle.circle(7.5*i,120) #画一段120度弧线
    turtle.penup()
    turtle.goto(px,py) #回到圆点位置
    turtle.setheading(an+90)
    turtle.pendown()
    turtle.circle(-7.5*i,120)
    turtle.setheading(an+100)
    turtle.circle(10.5*i,150)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(til)
    turtle.pensize(node/2+1)

#定义生成树
def draw(node,length,level,yu,button):
    turtle.pendown()
    tu=cos(radians(turtle.heading()+5))/8+0.25
    turtle.pencolor(tu*1.6,tu*1.2,tu*1.4)
    turtle.pensize(node/1.2)
    x=random.randint(0,10)  #生成随机数决定要画树枝还是飘落的叶子

    if level==top and x>6:
        turtle.forward(length)
        yu[level]=yu[level]-1
        c=random.randint(2,10)
        for i in range(1,c):
            leaf(turtle.xcor(),turtle.ycor(),node)
            if random.random()>0.3:
                turtle.penup()
                #飘落
                t1=turtle.heading()
                an1=-40+random.random()*40
                turtle.setheading(an1)
                dis=int(800*random.random()*0.5+400*random.random()*0.3+200*random.random()*0.2)
                turtle.forward(dis)
                turtle.setheading(t1)
                turtle.right(90)
                #画叶子
                leaf(turtle.xcor(),turtle.ycor(),node)
                turtle.left(90)
                t2=turtle.heading()
                turtle.setheading(an1)
                turtle.backward(dis)
                turtle.setheading(t2)
    elif level==top and x<7:
        turtle.penup()
        turtle.forward(length)
    elif level>3 and x>6:
        turtle.pendown()
        turtle.forward(length)
        c=random.randint(4,6)
        for i in range(3,c):
            leaf(turtle.xcor(),turtle.ycor(),node)
        leaf(turtle.xcor(),turtle.ycor(),node)
        button=1
    else:
        turtle.forward(length)
        yu[level]=yu[level]-1
    if node>0 and button==0:
        right=random.random()*5+17
        left=random.random()*20+19
        child_length=length*(random.random()*0.25+0.7)
        r=random.randint(0,1)
        if r==1:
            turtle.right(right)
            level=level+1
        else:
            turtle.left(right)
            level=level+1
        draw(node-1,child_length,level,yu,button)
        yu[level]=yu[level]+1
        if yu[level]>1:
            if r==1:
                turtle.left(right+left)
                draw(node-1,child_length,level,yu,button)
                turtle.right(left)
                yu[level]=yu[level]-1
            else:
                turtle.right(right + left)
                draw(node - 1, child_length, level, yu, button)
                turtle.left(left)
                yu[level] = yu[level] - 1
        else:
            if r==1:
                turtle.left(right+left)
                turtle.right(left)
            else:
                turtle.right(right+left)
                turtle.left(left)
    turtle.penup()
    turtle.backward(length)

def clear_all():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color('white')
    turtle.pensize(800)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fd(300)
    turtle.bk(600)


# 重定位海龟的位置
def go_to(x, y, state):
    turtle.pendown() if state else turtle.penup()
    turtle.goto(x, y)


def draw_heart(size):
    turtle.color('red', 'pink')
    turtle.pensize(2)
    turtle.pendown()
    turtle.setheading(150)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.circle(size * -3.745, 45)
    turtle.circle(size * -1.431, 165)
    turtle.left(120)
    turtle.circle(size * -1.431, 165)
    turtle.circle(size * -3.745, 45)
    turtle.fd(size)
    turtle.end_fill()


# 画出发射爱心的小人
def draw_people(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('black')
    turtle.setheading(0)
    turtle.circle(60, 360)
    turtle.penup()
    turtle.setheading(90)
    turtle.fd(75)
    turtle.setheading(180)
    turtle.fd(20)
    turtle.pensize(4)
    turtle.pendown()
    turtle.circle(2, 360)
    turtle.setheading(0)
    turtle.penup()
    turtle.fd(40)
    turtle.pensize(4)
    turtle.pendown()
    turtle.circle(-2, 360)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(20)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(40)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(-60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(60)
    turtle.setheading(-135)
    turtle.fd(60)
    turtle.bk(60)
    turtle.setheading(-45)
    turtle.fd(30)
    turtle.setheading(-135)
    turtle.fd(35)
    turtle.penup()


# 绘制文字
def draw_text(text, t_color, font_size):
    turtle.penup()
    turtle.goto(-350, 0)
    turtle.color(t_color)
    turtle.write(text, font=('宋体', font_size, 'normal'))
    time.sleep(2)
    clear_all()


# 爱心发射
def draw_():
    turtle.speed(0)
    draw_people(-250, 20)
    turtle.penup()
    turtle.goto(-150, -30)
    draw_heart(14)
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.color('pink')
    turtle.write('Biu~', font=('宋体', 60, 'normal'))
    turtle.penup()
    turtle.goto(-20, -60)
    draw_heart(25)
    turtle.penup()
    turtle.goto(-70, -200)
    turtle.color('pink')
    turtle.write('Biu~', font=('宋体', 60, 'normal'))
    turtle.penup()
    turtle.goto(200, -100)
    draw_heart(45)
    turtle.penup()
    turtle.goto(150, -200)
    turtle.color('pink')
    turtle.write('七夕快乐~', font=('宋体', 60, 'normal'))
    turtle.hideturtle()
    time.sleep(3)


def main():
    # 隐藏海龟
    hideturtle()
    turtle.setup(width=0.75,height=0.75)

    draw_text("Are You Readly？", "black", 60)
    draw_text("接下来", "skyblue", 60)
    draw_text("七夕快乐！", "pink", 95)
    draw_()
    # 使用mainloop防止窗口卡死
    mainloop()


#主函数
if __name__ == '__main__':
    turtle.setup(width=0.75,height=0.75)             #屏幕占比
    turtle.hideturtle()                            #隐藏
    turtle.speed(0)                              #速度0-9
    turtle.penup()
    turtle.left(90)
    turtle.backward(300)
    top=9
    yu=FR(top)
    yu.remove(yu[0])
    button=0
    draw(9,120,0,yu,button)
    turtle.write("    七夕快乐!\n",font=("微软雅黑",14,"normal"))
    turtle.write("  ~三只碎片",font=("微软雅黑",16,"normal"))
    time.sleep(3)
    turtle.clear()
    main()

