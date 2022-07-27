# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import random
from PIL import Image, ImageTk,ImageSequence
from threading import Timer
import time



meat = ['千张炒牛百叶', '大盘鸡拌面', '秘制鸡煲', '酱爆腰果鸡丁', '毛豆炒肉', '卤牛展','烤羊排','红烧牛肋条','卤猪蹄','绝味卤菜','麻辣香锅']
vegetable=['干锅包菜','蛋炒饭','番茄炒蛋','糖拌番茄','凉拌黄瓜','莲藕菠菜','肉末茄子','炒豆干','西兰花炒虾仁','醋溜土豆丝','烤红薯','腊肉炒花菜']
soup=['鸭汤','猪骨汤','鸡汤','芝麻糊','核桃糊']

window=tk.Tk()
window.title("老范私房菜：点菜盲盒")
#窗口大小
window.geometry("900x700")

l1=tk.Label(window, text="欢迎来到老范私房菜馆，请体验点菜盲盒",bg="#EAF6F6",fg="black",font=("STHeiti 26 bold"),width=36,height=3)
l1.pack()

#荤菜选择窗口
l2=tk.Label(window, text="请输入荤菜数量(1/2/3)其他数字会有惊喜哦:",bg="#E8A0BF",fg="black",font=("STHeiti 20 bold"),
            width=45,height=1)
l2.pack()


e1=tk.Entry(window,show=None,font=("Arial",20))
e1.pack()

#程序在框中输出所选菜品
var1=tk.StringVar()
l3=tk.Label(window,textvariable=var1,bg="#C4DFAA",fg="black",font=("STHeiti 22"),width=65,height=1)
l3.pack()

def rou():
   
   choice1=int(e1.get())
   
   if choice1 == 1:
       m1=random.sample(meat,1)
       var1.set(f"你选择的菜品为：{m1}")
   elif choice1 ==2:
       m2=random.sample(meat,2)
       var1.set(f"你选择的菜品为：{m2}")
   elif choice1 == 3:
       m3=random.sample(meat,3)
       var1.set(f"你选择的菜品为：{m3}")
       
   else:
       
       var1.set("不要太贪心哦！")
       img=Image.open('C:\\Users\\user\\Desktop\\blindmenugui\\noeat.png').resize((200, 128))
       global photo1
       photo1=ImageTk.PhotoImage(img)
       lab1=tk.Label(window,width=200,height=150,image=photo1)
       lab1.place(x=600,y=150)
       def disappear():
           lab1.place_forget()
       t=Timer(3.0,disappear)
       t.start()   
       
#设置一个按钮       
b1=tk.Button(width=10,height=1,text="开始选荤菜吧",command=rou)
b1.pack()

 #素菜选择窗口
l4=tk.Label(window, text="请输入素菜数量(1/2/3)其他数字会有惊喜哦:",bg="#3AB0FF",fg="black",font=("STHeiti 20 bold"),
            width=45,height=1)
l4.pack()


e2=tk.Entry(window,show=None,font=("Arial",20))
e2.pack()
 
var2=tk.StringVar()
l5=tk.Label(window,textvariable=var2,bg="#FFFFDE",fg="black",font=("STHeiti 22"),width=65,height=1)
l5.pack()

def cai():
    
    choice2=int(e2.get())
    
    if choice2 == 1:
        c1=random.sample(vegetable,1)
        var2.set(f"你选择的菜品为：{c1}")
    elif choice2 ==2:
        c2=random.sample(vegetable,2)
        var2.set(f"你选择的菜品为：{c2}")
    elif choice2 == 3:
        c3=random.sample(vegetable,3)
        var2.set(f"你选择的菜品为：{c3}")
        
    else:
        
        var2.set("不要太贪心哦！")
        img2=Image.open('C:\\Users\\user\\Desktop\\blindmenugui\\noway.png').resize((200, 128))
        global photo2
        photo2=ImageTk.PhotoImage(img2)
        lab2=tk.Label(window,width=200,height=150,image=photo2)
        lab2.place(x=600,y=250)
        def disappear():
            lab2.place_forget()
        t=Timer(3.0,disappear)
        t.start()   
        
        
b2=tk.Button(width=10,height=1,text="开始选素菜吧",command=cai)
b2.pack()        
       
#汤
l6=tk.Label(window,text="要喝汤吗？", bg="#D6D5A8",fg="black",font=("Arial 20 bold"),
            width=45,height=1)
l6.pack()

var3=tk.StringVar()
l7=tk.Label(window,textvariable=var3,bg="#D0C9C0",fg="black",font=("STHeiti 24"),width=45,height=1)
l7.pack()
def tangyes():
    return var3.set(f"你选择的汤为{random.sample(soup,1)}")
def tangno():
    
    img3=Image.open('C:\\Users\\user\\Desktop\\blindmenugui\\dd2.gif')
    iter = ImageSequence.Iterator(img3)
    for frame in iter:
            global pic            
            pic=ImageTk.PhotoImage(frame)
            lab3=tk.Label(window,width=200,height=150,image=pic)
            lab3.place(x=350,y=550)
            time.sleep(0.1)
            window.update_idletasks()  #刷新
            window.update()
            def disappear():
                 lab3.place_forget()
            t=Timer(3.0,disappear)
            t.start() 

    #global photo3
    #photo3=ImageTk.PhotoImage(img3)
    # lab3=tk.Label(window,width=200,height=150,image=photo3)
    # lab3.place(x=600,y=250)
    
    return var3.set("明白了！")
b3=tk.Button(window,width=10,height=1,text="YES",command=tangyes)
b4=tk.Button(window,width=10,height=1,text="NO",command=tangno)
b3.place(x=300,y=500)
#b3.pack()
b4.place(x=500,y=500)
#b4.pack()

window.mainloop()

input("please input any key to exit")