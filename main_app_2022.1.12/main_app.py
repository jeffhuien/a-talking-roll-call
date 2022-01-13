'''
Author: GAO--HUI
Date: 2022-01-10 14:09:37
LastEditors: GAO--HUI
LastEditTime: 2022-01-12 16:40:16
FilePath: \ss\main_app.py
'''

import time, os, sys
import random as r
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import pyttsx3 as sp
import base64

class App:

    # --------------------------------------------------界面构造---------------------------------------------------

    def __init__(self) -> None:
        self.ico=base64.b64decode('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')
        if not os.path.exists(os.path.join(os.getcwd(), 'ic.ico')):
                
            with open("ic.ico", "wb") as f:
                f.write(self.ico)

        self.root = Tk()
        self.root.geometry("960x350+330+330")
        self.root.resizable(0,0)
        self.root.configure(bg="#cde6c7")
        self.root.iconbitmap("ic.ico")  # 窗口图标设置
        # self.root.iconbitmap("风车.ico")  # 窗口图标设置
        self.root.title("by_计181髙輝\'\'")

        self.varstr = StringVar()  # 可变字符串
        self.varstr.set("天选之子就是你")

        self.source_namelist = []
        self.past_namelist = []
        self.longname = []
        self.T=0

        # self.x=StringVar()
        # self.y=StringVar()

        # self.lx=Label(self.root,textvariable=self.x).pack(side=BOTTOM,anchor=NW)
        # self.ly=Label(self.root,textvariable=self.y).pack(side=BOTTOM,anchor=NW)

        self.l1 = Label(
            self.root,
            textvariable=self.varstr,
            font=("ZHSRuiXian-yolan", 40, "italic"),
            bg="#000000",
            fg="#00BFFF",
            height=1,
            width=29,
        )

        self.l1.pack(side=TOP, anchor=CENTER, fill=X)

        self.timeLabel = Label(
            self.root,
            text='现在时间：'+time.strftime("%Y/%m/%d %H:%M:%S"),
            font=("楷体", 15, "italic"),
            bg=self.root.cget("bg"),
        )
        self.timeLabel.place(rely=0.2, relx=0)

        # self.l2 = Label(
        #     self.root,
        #     #text="同学你别慌 运气来了挡也挡不住",
        #     font=("华文彩云", 18, "italic"),
        #     fg="#ef5b9c",
        #     bg=self.root.cget("bg"),
        # )
        # self.l2.place(relx=0.5, rely=0.24, anchor=CENTER)
        
        #############################功能区#####################################

        self.l0 = Label(
            self.root,
            text="当前选择->",
            font=("songti", 12),
            height=1,
            width=10,  # , bg='#FF66CC'
            anchor=W,
        )
        self.l0.place(relx=0.71-0.07, rely=0.2)

        self.online = ttk.Combobox(self.root, width=5)
        self.online["value"] = ["联网", "不联网"]
        self.online.current(1)
        self.online.place(relx=0.80-0.07, rely=0.2)

        self.voice = ttk.Combobox(self.root, width=7)
        self.voice["value"] = ["读出结果", "不读"]
        self.voice.current(0)
        self.voice.place(relx=0.80-0.01, rely=0.2)

        self.txtlist = ttk.Combobox(
            self.root, width=16  # , textvariable=self.combobox_text
        )
        self.txtlist.bind("<<ComboboxSelected>>", self.show)

        self.txtlist.place(relx=0.87-0.01, rely=0.2)

        self.scr = Scrollbar(self.root)  # 添加一个滚动条与Listbox配合使用
        self.beforename = Listbox(
            self.root, height=9, width=45, relief="flat", fg="#000", font=("等线", 16)
        )
        self.scr.config(command=self.beforename.yview)
        self.beforename.config(yscrollcommand=self.scr.set)
        self.scr.place(rely=0.3, relx=0.55, height=210, width=21)
        self.beforename.place(relx=0.03, rely=0.3)


        self.b1 = Button(
            self.root, text="连点", command=self.one1, width=8, height=1, relief=FLAT
        )
        self.b1.place(relx=0.71, rely=0.49)
        self.b2 = Button(
            self.root, text="单点", command=self.one, width=8, height=1, relief=FLAT
        )
        self.b2.place(relx=0.89, rely=0.49)

        self.b4 = Button(
            self.root,
            text="点名4",
            command=self.four,
            width=8,
            height=1,
            relief=FLAT,  # bg='#f46ec6'
            bg="#00a6ac",
        )
        self.b4.place(relx=0.8, rely=0.6)

        self.b3 = Button(
            self.root, text="朗读", command=self.speak, width=8, height=1, relief=FLAT
        )
        self.b3.place(relx=0.71, rely=0.69)

        self.b5 = Button(
            self.root, text="清空名单", command=self.clear, width=8, height=1, relief=FLAT
        )
        self.b5.place(relx=0.89, rely=0.69)

        self.b6 = Button(
            self.root, text="现写现抽", command=self.now, width=8, height=1, relief=FLAT
        )
        self.b6.place(relx=0.8, rely=0.8)

        ###################################底部######################################

        self.l4 = Label(
            self.root,
            text="历史数据请移步至同文件夹的<log.log>",
            font=("ZHSRuiXian-yolan", 16),
            bg=self.root.cget("bg"),
            fg="#826858",
            height=1,
            width=72,
            anchor=E,
        )
        self.l4.place(relx=0, rely=0.91)

    # --------------------------------------------------功能实现---------------------------------------------------

    # def size(self):  #返回窗体大小
    #     self.x.set(str(self.root.winfo_width()))
    #     self.y.set(self.root.winfo_height())
    #     self.root.after(1,self.size)

    def loadfile(self, file: str):

        with open(os.path.join("./name", file), "r", encoding="utf-8") as f:
            readlines = f.read().splitlines()
            if readlines == []:
                messagebox.showinfo("提示", "该文件为空哦")
                self.source_namelist = []
            else:
                self.source_namelist = readlines
                print("名单：", self.source_namelist)
                # self.source_namelist.append(i.rstrip("\n"))  # 去掉换行符
        # return self.source_namelist

    def show(self, root):
        self.loadfile(self.txtlist.get())
        self.nowname=[]
        self.T=0
        print("show执行了")
        print("选择了：" + self.txtlist.get())

    def choicename(self, x: int):  # 程序核心
        self.name = []
        for i in range(x):
            r.seed()
            self.name.append(r.choice(list(set(self.source_namelist) - set(self.name))))
        s = ""
        for i in self.name:
            s += str(i) + "    "
        return [self.name, s]

    def loadfilelist(self):
        self.filelist = []
        if os.path.exists(os.path.join(os.getcwd(), "name")) and os.listdir(
            os.path.join(os.getcwd(), "name")
        ):

            for self.根目录, self.子目录, self.文件 in os.walk(
                os.path.join(os.getcwd(), "name")
            ):
                for j in self.文件:
                    # if self.文件.endswith('txt'):
                        # self.filelist.append(j)
                    if j[-3::] == "txt":
                        self.filelist.append(j)
            self.txtlist["value"] = self.filelist
        elif not os.path.exists(os.path.join(os.getcwd(), "name")):
            self.root.withdraw()
            os.makedirs(os.path.join(os.getcwd(), "name"))
            messagebox.showwarning(
                "error", "目录中不存在name文件夹，已自动创建name文件夹，请将花名册放入name文件夹后重新打开该程序！"
            )

            sys.exit()

        else:
            # if not os.listdir(os.path.join(os.getcwd(), "name")):
            messagebox.showwarning(
                "error", "name文件夹为空，建议将花名册放入name文件夹后重新打开该程序！\n您也可以直接使用本程序的现写现抽功能"
            )

        # return self.filelist

    def source_GUI(self):
        self.l1.config(height=1)

        self.l1.pack(side=TOP, anchor=CENTER, fill=X)
        self.timeLabel.place(rely=0.2, relx=0)

        self.l0.pack_forget()
        self.l0.place(relx=0.71-0.07, rely=0.2)

        self.online.pack_forget()
        self.online.place(relx=0.80-0.07, rely=0.2)

        self.voice.pack_forget()
        self.voice.place(relx=0.80-0.01, rely=0.2)

        self.txtlist.pack_forget()
        self.txtlist.place(relx=0.87-0.01, rely=0.2)

        self.beforename.place(relx=0.03, rely=0.3)
        self.scr.place(rely=0.3, relx=0.55, height=210, width=21)

        self.b1.place(relx=0.71, rely=0.49)
        self.b2.place(relx=0.89, rely=0.49)
        self.b3.place(relx=0.71, rely=0.69)
        self.b4.place(relx=0.8, rely=0.6)
        self.b5.place(relx=0.89, rely=0.69)
        self.b6.place(relx=0.8, rely=0.8)

    def four(self):
        if len(self.source_namelist)<=0:
            messagebox.showinfo('提示','剩余0人\n您可以重新选择名单列表')

        # if len(self.source_namelist) <= 0:
            # self.loadfile(self.txtlist.get())

        if self.l1["height"] == 4:
            self.source_GUI()

        if len(self.source_namelist) < 4:
            messagebox.showinfo("提示", "未抽人数剩余%d，建议单抽" % len(self.source_namelist))
        else:
            for i in range(9):
                time.sleep(0.031)
                self.past_namelist = self.choicename(4)
                self.varstr.set(self.past_namelist[1])
                self.root.update()
            print(self.past_namelist[0])
            self.beforename.insert(END, self.past_namelist[1])
            self.bgcolor()
            self.log()
            self.speak()
        self.source_namelist = list(
            set(self.source_namelist) - set(self.past_namelist[0])
        )

    def one1(self):
        if len(self.source_namelist)<=0:
            messagebox.showinfo('提示','剩余0人\n您可以重新选择名单列表')


        # if len(self.source_namelist) <= 0:
        #     self.loadfile(self.txtlist.get())

        self.l1.configure(height=4, wraplength=940)

        self.timeLabel.place_forget()
        self.beforename.place_forget()
        self.scr.place_forget()

        self.l0.pack(side=LEFT, anchor=NW)
        self.online.pack(side=LEFT, anchor=NW)
        self.voice.pack(side=LEFT, anchor=NW)
        self.txtlist.pack(side=LEFT, anchor=NW)
        # self.voice.pack()
        # self.b1.place_forget()
        # self.b2.place_forget()
        # self.b3.place_forget()
        # self.b5.place_forget()
        # self.b4.place_forget()
        self.b6.place_forget()

        self.b5.pack(side=RIGHT, anchor=NW)
        self.b2.pack(side=RIGHT, anchor=NW)
        self.b3.pack(side=RIGHT, anchor=NW)
        self.b4.pack(side=RIGHT, anchor=NW)
        self.b1.pack(side=TOP, anchor=CENTER)
        # self.b6.pack(side=RIGHT,anchor=NW)

        self.past_namelist = self.choicename(1)
        self.longname.append(self.past_namelist[0])
        self.varstr.set(self.longname)

        self.source_namelist = list(
            set(self.source_namelist) - set(self.past_namelist[0])
        )
        self.log()

    def one(self):

        if self.l1["height"] == 4:
            self.source_GUI()

        if self.T==1 and len(self.source_namelist)<=0:
            messagebox.showinfo('现写现抽','剩余0人\n您可以重新选择名单列表或继续使用现写现抽！')
        
        if len(self.source_namelist)<=0:
            messagebox.showinfo('提示','剩余0人\n您可以重新选择名单列表')

        # if len(self.source_namelist) <= 0:
            # self.loadfile(self.txtlist.get())

        for i in range(9):
            time.sleep(0.031)
            self.past_namelist = self.choicename(1)
            self.varstr.set(self.past_namelist[0])
            self.root.update()

        print(self.past_namelist[0])
        self.speak()
        self.source_namelist = list(
            set(self.source_namelist) - set(self.past_namelist[0])
        )
        self.log()
        self.beforename.insert(END, self.past_namelist[1])
        self.bgcolor()

    def clear(self):
        self.varstr.set("天选之子就是你")

    def now(self):
        self.source_namelist=[]
        self.win1 = Toplevel()
        self.win1.geometry("540x350+150+150")
        self.win1.overrideredirect(True)#取消标题栏
        self.win1.title("输入名单")
        self.win1text = Text(
            self.win1,
            height=14,
            width=35,
            highlightcolor="red",
            highlightthickness=1,
            font=(18),
            relief=FLAT,
        )
        self.win1text.pack(side=LEFT, anchor=NE, padx=3)

        self.scr = Scrollbar(self.win1)  # 添加一个滚动条与listbox配合使用
        self.scr.config(command=self.win1text.yview)
        self.win1text.config(yscrollcommand=self.scr.set)
        self.win1text.focus_set()

        self.scr.pack(side=LEFT, fill=Y, anchor=SW)
        self.win1ideatext = Label(
            self.win1, font=("bold", 15), text="格式要求:\n一行一名"
        ).pack(side=TOP, anchor=SE)

        self.win1button = Button(
            self.win1,
            text="确定",
            width=11,
            command=self.win1ok,
            relief=FLAT,  # bg='#f46ec6'
            bg="#00a6ac",
        ).pack(side=RIGHT, anchor=SE)

    def win1ok(self):
        self.source_namelist=[]
        self.T=1
        self.source_namelist =[i for i in  (self.win1text.get("0.0","end").replace(" ","")).split("\n") if i != ''] 
        # self.source_namelist = self.nowname
        print(self.source_namelist)
        messagebox.showinfo("现抽现点", "名单已更新为刚才输入的，若要更换名单请重新在名单列表中选择！")
        self.win1.destroy()

    def speak(self):
        rate = sp.init()
        rate.setProperty("rate", 150)  # 调整语速为150
        rate.setProperty("voice", 0)  # 调整发音人为0  {0,1}
        print("当前选择：{}".format(self.online.get()))

        if self.voice.get()=='不读':
            pass
        else:        
            if self.l1.cget("height") == 4 or self.varstr.get() == "天选之子就是你":
                sp.speak(self.varstr.get())
            else:
                # 后期可在此处添加联网API
                if self.online.get() == "不联网":
                    sp.speak(self.past_namelist[0])
                else:
                    sp.speak(self.past_namelist[0])

                    # 在此处写联网api的  speak()函数 {发声函数} 并注释掉上一行

    def bgcolor(self):
        for i in range(self.beforename.size()):
            if i % 2 == 0:
                self.beforename.itemconfig(i, {"bg": "#DFF6FF"})
            else:
                self.beforename.itemconfig(i, {"bg": "#F5FAFE"})

    def log(self):
        with open("log.log", "a+", encoding="utf-8") as w:
            w.write(f'{time.strftime("%Y-%m-%d %H:%M:%S"):=^80}' + "\n")
            w.write(str(self.past_namelist[0]) + "\n\n")

    def timeup(self):
        self.timeLabel.configure(text="现在时间：" + time.strftime("%Y/%m/%d %H:%M:%S"))
        self.root.after(900, self.timeup)

    # def end(self):
    #     self.txtlist.current(0)
    #     self.loadfile(self.txtlist.get())
    #     self.root.mainloop()

    def main(self):

        self.loadfilelist()
        # self.loadfile(self.loadfilelist()[0])
        if self.filelist != []:
            print("value", self.txtlist["value"])
            self.txtlist.current(0)
            self.loadfile(self.txtlist.get())
        self.timeup()
        self.root.mainloop()
        # self.end()


if __name__ == "__main__":
    # app = App()
    # app.main()
    App().main()

#打包
# pyinstaller -F  -w -i ic.ico -p C:\Users\gaohui\AppData\Local\Programs\Python\Python38\Lib\site-packages test.py