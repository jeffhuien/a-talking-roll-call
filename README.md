# 一个能说话的点名器

#### 介绍
这是我自学python做的一个能基本实现说话的点名器，界面我不是很在行所以就有点丑吧。欢迎大家来给这个小东西添砖加瓦，代码写的很烂，大家不要见怪哈

#### 软件架构
软件架构说明
python的版本我用的是3.9.6 ，该版本经测试win7是不能用的，版本降到3.8，win7能用但是不能说话，具体原因我也不清楚

#### 安装教程

1.  python 3.9.6，3.7应该也行，我以前是3.7但是打包出了点问题，尽量3.8吧
2.  pyttsx3库

#### 使用说明

1.  pip install pyttsx3 #安装这个第三方库用于发声
2.  ic.ico 和 name.txt 这两个东西与main.py放在同一文件夹下就可以使用了，这两个东西必不可少，名字也不可变
3.  要更换名单信息，直接替换name.txt内容就行，格式是一行一名
4.  读取excel的功能能做的，就是做了感觉没啥用。读txt功能上没啥差别是吧

#### 界面展示
![输入图片说明](https://images.gitee.com/uploads/images/2021/0807/141820_a29d0a95_5591477.png "界面.png")
![输入图片说明](https://images.gitee.com/uploads/images/2021/0807/141838_513f477a_5591477.png "效果.png")
