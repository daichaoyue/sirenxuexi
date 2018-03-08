# -*- coding: utf-8 -*-
#从 sys模块导入 argv
from sys import argv

#解包 变量 input_file
script, input_file = argv

#建立函数 print—all  （参数f） ：
def print_all(f):
#打印 参数。读取函数
	print f.read()

#建立函数 rewind（参数f） ：
def rewind(f):
#参数f 。seek（0）移动读取指针到0位置
	f.seek(0)

#建立函数print_a_line （参数line_count，  参数f） ：	
def print_a_line(line_count, f):
#打印 参数line_count， 参数f。 readline（）函数 读取文件行函数
	print line_count, f.readline()

#定义变量 current_file  = 打开函数 打开顶层 input_file输入的文件	
current_file = open(input_file)

#打印 首先 让我们 打印  整个文件 \n 换行符
print "First let's print the whole file:\n"

#自建函数  （打印参数的read（）读取的文件) current_file就是这里参数
print_all(current_file)

# 打印 现在 我们 倒回     有点  像     磁带
print "Now let's rewind, kind of like a tape."

#自建函数  （让参数文件 用seek（0）函数，让读取指针回到0点）
rewind(current_file)

# 打印  让我秒 打印  三行
print "Let's print three lines:"

# 定义变量 current_line  =  整数1
current_line = 1
# 自建函数 （第一个参数取值不变，  第二个参数用readline（）读取行函数取返回的值
# 第二个参数，经过函数传递，这个变量存储的内容已经是  用户初始输入的 
# input_file这个文件的值了，也就是初始TXT文档
print_a_line(current_line, current_file)

#与上类似，   这里用了变量自增1，可以用 += 这个运算符实现
current_line = current_line + 1
print_a_line(current_line, current_file)

#与上一样
current_line = current_line + 1
print_a_line(current_line, current_file)
