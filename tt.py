# print('파이썬의 셰계에 오신 것을 환영합니다')
# import streamlit as st
# import time
# import turtle
# import random

# t = turtle.Turtle()
# t.shape('turtle')

# screen = turtle.Screen()
# im = 'rabbit.gif'

# t1=turtle.Turtle()
# t2=turtle.Turtle()

# screen.addshape(im)
# # t1.shape(im)
# t2.shape('turtle')

# t1.penup()
# t1.shapesize(2)
# t1.goto(-300,0)

# t2.penup()
# t2.shapesize(2)
# t2.goto(-300,-200)

# for i in range(50):
#     di = random.randint(1,30)
#     t1.forward(di)
#     d2 = random.randint(1,30)
#     t2.forward(d2)


# turtle.done()


# def rec(x, y, Lx, Ly):
#     t.up()
#     t.goto(x,y)
#     t.down()

#     for i in range(2):
#         turtle.bgcolor('yellow')
#         t.forward(Lx)
#         t.left(90)
#         t.forward(Ly)
#         t.left(90)

# rec(-200,0,100,50)
# rec(0,0,100,150)
# rec(200,0,100,100)

# def user_sum(n):
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     s


    
# user_sum(100)
# user_sum(200)




# import random as r
# a1 = r.randint(1,45)
# print(a1)


# 난수에 퍼센트를 구하는 식
# ramdom number
# randint 


import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

c1= st.sidebar.radio('선의 색을 선택하시오',['red','green','blue'])
s1= st.sidebar.radio('선의 스타일을 선택하시오.',['-','--'])
m1= st.sidebar.radio('점의 스타일을 선택하시오.',['o','s'])

holy= []
y = []
for i in range(-20,21,3):
    holy.append(i)
    y.append(-2*i*1 + 3*i + 5)

plt.plot(holy, y, color = 'c1', linestyle = 's1', marker = 'm1' )
st.pyplot(fig)