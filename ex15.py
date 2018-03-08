# -*- coding: utf-8 -*-
#这个课程需要事前把 要导入的TXT文件写出来，保存在工作文件夹里
#从 sys（内置模块）  导入 argv（用户输入的参数）
from sys import argv

#脚本默认【0】  解包变量filename  从argv里
scrirt, filename = argv

#定义变量txt = open（）打开函数打开文件返回的值
txt = open(filename)

#打印 这是你的文件  %r    带入解包的用户输入的参数
print "Here's your file %r :" % filename
#打印 txt（上面定义过） 用（.）句号衔接下面的函数 read（），打开函数，
#把open（）返回的值 读出来
print txt.read()

#打印  再次 打字 filename
print "Type the filename again:"
# 定义变量 file_again = 用户输入函数  给个提示符>
file_again = raw_input(">" )

# 定义变量 txt_again = 打开函数（file_again）
txt_again = open(file_again)

#打印 txt_again   “.”    读取函数（） 
print txt_again.read()