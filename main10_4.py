#!/usr/bin/env python
# coding=utf-8

#name: GAO-HUI
# Date: 2021-06-22 15:22:57
#LastEditTime: 2021-10-04 01:06:24
# #点名

import os
import random
import threading
import time
import tkinter.messagebox
import winsound
from tkinter import *
from tkinter import ttk

import pyttsx3 as sp  # 需要安装pyttsx3 第三方库 执行pip命令 pip install pyttsx3
from python_sdk.tcloud_tts import txspeak

名单备份 = []
namels = []
已抽名单 = []

######################函数区###############################


def loadfile(text):
    global 名单备份, namels
    f = open(text, 'r', encoding="UTF-8")
    namels = f.read().splitlines()
    名单备份 = namels[:]
    f.close()
    print(namels)


def num(x):
    global 已抽名单, namels
    n = 0
    while n < x:
        n += 1
        random.seed()
        name = random.choice(namels)
        namels.remove(name)
        已抽名单.append(name)
        
        if len(namels) < 3:
            namels.clear()
            namels = 名单备份[:]
        s=''
        for i in 已抽名单:
            
            s+=i+'    '
        # if x==1:
        #     names1.append(name)
        #     return names1
        #     # return name
    # return 已抽名单
    return s


def 插入项目():
    dir1 = os.getcwd()
    list1 = []
    for 根目录, 子目录, files in os.walk(dir1):
        for file in files:
            # print(根目录, '--->', file)
            if file.endswith('txt'):
                list1.append(file)
    txtlist['value'] = list1
    # li['value']=['1','2','3','4','5','6','7','8']


def show(root):
    loadfile(txtlist.get())
    print('选择了：'+txtlist.get())


def txsp():
    if online.get() == '不联网':
        engine = sp.init()
        # rate=engine.getProperty('rate')
        engine.setProperty('rate', 130)  # 设置语速
        sp.speak(namelist.get())
    else:
        txspeak(namelist.get())
        print(namelist.get())
        # os.remove('test.wav')
        winsound.PlaySound('test.wav', winsound.SND_FILENAME)


def four():
    for i in range(3):  # 循环几次就更新几次标签
        已抽名单.clear()
        namelist.set(num(4))
        time.sleep(0.1)
        root.update()
    log()
    lastname.insert(END,namelist.get())
    bgcolor()
    txsp()
    print(已抽名单, end="")
    print('还剩', len(namels), '人')
    已抽名单.clear()


def one1():
    namelist.set(num(1))
    print(namelist.get())
    log()
    lastname.insert(END,已抽名单[-1])
    bgcolor()

def one():
    for i in range(3):  # 循环几次就更新几次标签
        已抽名单.clear()
        namelist.set(num(1))
        time.sleep(0.1)
        root.update()
    log()
    lastname.insert(END,namelist.get())
    txsp()
    print(len(namels))
    已抽名单.clear()


def clear():
    namelist.set("天选之子就是你")
    已抽名单.clear()


def chi():  # 调用后可以返回窗体的尺寸
    print("当前窗口的宽度为", root.winfo_width(), end="  ")
    print("当前窗口的高度为", root.winfo_height())


def log():  # 记录日志文件
    b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f = open('log.log', 'a+', encoding="utf-8")
    f.write(f'{b:=^50}'+'\n')
    f.write(str(已抽名单)+'\n')
    f.write('\n')
    f.close


def click(event):
    print("当前位置：", event.x/100, 1/event.y)


def timeup():
    r = threading.Timer(1, timeup)
    r.setDaemon(True)
    r.start()
    timetext.set('现在时间:'+time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
    root.update()

def bgcolor():
    for i in range(lastname.size()):
        if i % 2==0:

            lastname.itemconfig(i,{'bg':'#EE82EE'})
        else:
            lastname.itemconfig(i,{'bg':'white'})
'''
Label(父对象, text="标签内容", width="宽度", height="高度", anchor="对齐方式")
width ：标签宽度，单位（字符）
height：标签的高度 单位（行）
anchor：对齐方式 可选内容包括 n:靠上 w靠左 s靠下 e靠右 或者组合使用，，如nw 左上方对齐
'''

###########################构造界面##################################

root = Tk()
root.withdraw()  # 先让窗体不显示
root.configure(bg='#EFD3D2')
root.resizable(0,0)


root.geometry("950x350")
root.title("by_髙輝\"")
namelist = StringVar()
namelist.set("天选之子就是你")
combobox_text = StringVar()
# strVar1 = StringVar()
timetext = StringVar()

# lastname.set('')
# tkinter.messagebox.showinfo("友情提示","!!!!!将name.txt与本程序放在同一文件夹内即可开始使用!!!!!\n!!!!!必须是name.txt!!!!!\n!!!!!如果打不开请检查该txt是否为UTF-8编码!!!!!!")
tkinter.messagebox.showinfo("欢迎", "让我们开始愉快的点名时刻吧！！！")
root.wm_deiconify()  # 让窗体显示出来
root.bind("<Button-1>", click)

#
################################顶部##################################

l1 = Label(root, textvariable=namelist, font=('ZHSRuiXian-yolan',
           30,), bg='#000000', fg='#00BFFF', height=1, width=37)
# l1.grid(row=0,column=0,columnspan=5)
# l1.pack(side=TOP, fill=Y)
l1.place(relx=0,rely=0)
timelabel = Label(root, textvariable=timetext, font=('楷体',15),
                  bg='lightblue').place(rely=0.2, relx=0)
l2 = Label(root, text="同学你别慌 运气来了挡也挡不住", font=(
    '华文彩云', 18, 'italic'), fg='#168AC4', bg=root.cget('bg'))
l2.place(relx=0.5, rely=0.23, anchor=CENTER)
# l2.grid(row=3,column=0,columnspan=3)
# l3 = Label(root, textvariable=lastname, font=('ZHSRuiXian-yolan', 24,),
#            bg=root.cget('bg'), fg='#000', height=1, width=43, anchor=W)
# # l3.grid(row=4,column=0,columnspan=5)
# l3.place(relx=0, rely=0.5)
timeup()
#############################功能区#####################################

l0 = Label(root, text='当前选择->', font=('songti',12), height=1,width=10, bg='#FF66CC', anchor=W)
l0.place(relx=0.71, rely=0.2)

online = ttk.Combobox(root, width=5)
online['value'] = ['联网', '不联网']
online.current(0)
online.place(relx=0.80, rely=0.2)

txtlist = ttk.Combobox(root, textvariable=combobox_text, height=1,width=12)
txtlist.bind('<<ComboboxSelected>>', show)
插入项目()
txtlist.current(0)

scr = Scrollbar(root)#添加一个滚动条与listbox配合使用


lastname=Listbox(root,height=9,width=45,highlightcolor='blue',relief='flat',fg='#000',font=('songti',16))
scr.config(command=lastname.yview)

lastname.config(yscrollcommand=scr.set)
scr.place(rely=0.3,relx=0.55,height=202,width=21)
# scr.pack()
lastname.place(relx=0.03,rely=0.3)

# strVar1.set("当前选择："+txtlist.get())
txtlist.place(relx=0.87, rely=0.2)
# li.grid(row=2,column=4,pady=1)

b1 = Button(root, text="连点", command=one1, width=8, height=1, relief=FLAT)
# b1.pack(side=LEFT, fill=X, padx=40)
# b1.grid(row=2,column=1)
b1.place(relx=0.71,rely=0.49)
b2 = Button(root, text="单点", command=one, width=8, height=1, relief=FLAT)
# b2.pack(side=LEFT, fill=X, padx=40)
# b2.grid(row=2,column=2)
b2.place(relx=0.89,rely=0.49)

b4 = Button(root, text="点名4", command=four, width=8,
            height=1, relief=FLAT, bg='#f46ec6')
# b4.pack(side=LEFT, fill=X, padx=40)
# b4.grid(row=2,column=3)
b4.place(relx=0.8,rely=0.6)


b3 = Button(root, text="朗读", command=txsp, width=8, height=1, relief=FLAT)
# b3.pack(side=LEFT, fill=X, padx=40)
# b3.grid(row=2,column=4)
b3.place(relx=0.71,rely=0.69)


b5 = Button(root, text="清空名单", command=clear, width=8, height=1, relief=FLAT)
# b5.pack(side=LEFT, fill=X, padx=40)
# b5.grid(row=2,column=5)
b5.place(relx=0.89,rely=0.69)

###################################底部######################################

l4 = Label(root, text="历史数据请移步至同文件夹的<log.log>", font=('ZHSRuiXian-yolan',
           20), bg='#000000', fg='#f46ec6', height=1, width=58, anchor=CENTER)
# l2.pack(side=BOTTOM,fill=X)
# l4.grid(row=6,column=0,columnspan=5)
l4.place(relx=0, rely=0.89)

# l2.place(relx=0.5,rely=0.93,anchor=CENTER)
# Label(父对象, text="标签内容", font=( '字体', 字号, 粗体, 斜体, 下划线, 删除线))
#                                                 粗体：bold 斜体：italic 下划线：underline 删除线：overstrike

try :
    loadfile(txtlist.get())
    root.iconbitmap('ic.ico')  # 窗口图标设置
    

except :
    tkinter.messagebox.showwarning('错误', '出错啦，原因是：name.txt或者ic.ico文件不存在')
    # os._exit()
root.mainloop()
#   pyinstaller -F -w -i ic.ico -p  C:\Users\AAX\AppData\Local\Programs\Python\Python38\Lib\site-packages  main.py
#   打包命令  -p 后面的路径是自己电脑python安装的第三方包的路径，需要自己替换为自己电脑的路径
