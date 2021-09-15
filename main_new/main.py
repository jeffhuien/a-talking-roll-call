#!/usr/bin/env python
# coding=utf-8
#name: GAO-HUI
#Date: 2021-06-22 15:22:57
#LastEditTime: 2021-09-13 13:28:48
# #点名

import random,time

from tkinter import *
import tkinter.messagebox
import pyttsx3 as sp        #需要安装pyttsx3 第三方库 执行pip命令 pip install pyttsx3

root=Tk()
root.withdraw()#先让窗体不显示
root.configure(bg='#EFD3D2')
root.resizable(0,0)

try:
    namels = []
    global 名单备份
    名单备份 = []
    已抽名单 = []
    f = open('name.txt', 'r', encoding="UTF-8")
    namels = f.read().splitlines()
    名单备份 = namels[:]
    f.close()

    def num(x):
        global namels,name, 已抽名单
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
        return 已抽名单

    def spa():
        engine = sp.init()
        # rate=engine.getProperty('rate')
        engine.setProperty('rate', 130)  # 设置语速
        # volume = engine.getProperty('volume')
        # print(f'语音音量：{volume}')
        # 设置新的语音音量，音量最小为 0，最大为 1
        # engine.setProperty('volume', 1.0)
        # engine.say(l1.cget('text'))
        sp.speak(l1.cget('text'))

    def si():
        for i in range(3):  # 循环几次就更新几次标签
            已抽名单.clear()
            var.set(num(4))
            time.sleep(0.1)
            root.update()
        log()
        spa()
        print(已抽名单, end="")
        print('还剩', len(namels), '人')
        已抽名单.clear()

    def one1():
        var.set(num(1))
        log()
    def one():
        for i in range(3):  # 循环几次就更新几次标签
            已抽名单.clear()
            var.set(num(1))
            time.sleep(0.1)
            root.update()
        log();spa()
        print(len(namels))
        已抽名单.clear()

    def clear():
        var.set("天选之子就是你")
        已抽名单.clear()

    def chi():#调用后可以返回窗体的尺寸
        print("当前窗口的宽度为", root.winfo_width())
        print("当前窗口的高度为", root.winfo_height())

    def log():#记录日志文件
        b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f = open('log.log', 'a+', encoding="utf-8")
        f.write(f'{b:=^50}'+'\n')
        f.write(str(已抽名单)+'\n')
        f.write('\n')
        f.close

    '''
    Label(父对象, text="标签内容", width="宽度", height="高度", anchor="对齐方式")
    width ：标签宽度，单位（字符）
    height：标签的高度 单位（行）
    anchor：对齐方式 可选内容包括 n:靠上 w靠左 s靠下 e靠右 或者组合使用，，如nw 左上方对齐
    '''

    root.iconbitmap('ic.ico')  # 窗口图标设置

    root.geometry("734x250")
    root.title("by_髙輝\"")
    var=StringVar()
    var.set("天选之子就是你")
    # tkinter.messagebox.showinfo("友情提示","!!!!!将name.txt与本程序放在同一文件夹内即可开始使用!!!!!\n!!!!!必须是name.txt!!!!!\n!!!!!如果打不开请检查该txt是否为UTF-8编码!!!!!!")
    tkinter.messagebox.showinfo("欢迎","让我们开始愉快的点名时刻吧！！！")
    root.wm_deiconify()#让窗体显示出来

    def FocusOut(event):
        log()

    l1=Label(root,textvariable=var,font=('ZHSRuiXian-yolan',20,),bg='#000000',fg='#00BFFF',height=1,width=300)
    l1.pack(side=TOP,fill=Y)

    b1=Button(root,text="连点",command=one1,width=8,height=1,relief=FLAT)
    b1.pack(side=LEFT,fill=X,padx=40)
    b1.bind("<FocusIn>")
    b1.bind("<FocusOut>",FocusOut)
    b2=Button(root,text="单点",command=one,width=8,height=1,relief=FLAT)
    b2.pack(side=LEFT,fill=X,padx=40)

    b4=Button(root,text="点名4",command=si,width=8,height=1,relief=FLAT,bg='#f46ec6')
    b4.pack(side=LEFT,fill=X,padx=40)

    b3=Button(root,text="朗读",command=spa,width=8,height=1,relief=FLAT)
    b3.pack(side=LEFT,fill=X,padx=40)

    b5=Button(root,text="清空名单",command=clear,width=8,height=1,relief=FLAT)
    b5.pack(side=LEFT,fill=X,padx=40)

    l2=Label(root,text="历史数据请移步至同文件夹的<log.log>",font=('ZHSRuiXian-yolan',20),bg='#000000',fg='#f46ec6',height=1,width=400)
    # l2.pack(side=BOTTOM,fill=Y)
    l2.place(relx=0.5,rely=0.93,anchor=CENTER)
    # Label(父对象, text="标签内容", font=( '字体', 字号, 粗体, 斜体, 下划线, 删除线))
    #                                                 粗体：bold 斜体：italic 下划线：underline 删除线：overstrike
    l4=Label(root,text="同学你别慌      同学你别慌      同学你别慌",font=('华文彩云',18,'italic'),fg='#168AC4',bg='#EFD3D2')
    # l2.pack(side=BOTTOM,fill=Y)
    l4.place(relx=0.5,rely=0.3,anchor=CENTER)

    root.mainloop()
except Exception as e:
    tkinter.messagebox.showwarning('错误','出错啦，原因是：name.txt或者ic.ico文件不存在')

#   pyinstaller -F -w -i ic.ico -p  C:\Users\AAX\AppData\Local\Programs\Python\Python38\Lib\site-packages  main.py   
#   打包命令  -p 后面的路径是自己电脑python安装的第三方包的路径，需要自己替换为自己电脑的路径