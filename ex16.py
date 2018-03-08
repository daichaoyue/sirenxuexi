# -*- coding: utf-8 -*-
#从 sys 导入 argv
from sys import argv

#脚本， 解包变量并命名  =argv
script, filename = argv

# 打印 我们 将要  删除   %r  带入% 解包出来的filename
print "We're going to erase %r/" % filename
#打印 如果 你不想  要  这样  按ctrl+c 
print "If you don't want that, hit CTRL-C(^C)."
# 打印 如果 你 想 这样   打 return  （语句：将结果返回调用的地方，并将程序控制器一起返回)
print "If you do want that, hit RETURN."

# 获取用户输入
raw_input("?")

#打印  打开这个文件
print "Opening the file..."
#定义变量 target（目标）  = 打开 函数（上面解包的变量，逗号， 
#"w" 特殊的单字符字符串，表示文件访问模式， write简写，写入模式
# “r” read 读取模式  “a” append 追加模式
target = open(filename, "w")

# 打印 截断 这个文件
print "Truncating the file.  Goodbye!"
# 变量target 句号， 截断函数（） 括号可跟参数，跟了参数后，将参数后面的字符删除
target.truncate()

# 打印 现在我要 你 输入 三行
print "Now I'm going to ask you for three lines."

#定义变量line1 = 用户输入（提示用户line1：）
line1 = raw_input("line 1: ")
#类似
line2 = raw_input("line 2: ")
#类似
line3 = raw_input("line 3: ")

#打印 我要 写 三行 放进 文件
print "I'm going to write these to the file."

#变量target 句号 写入函数（第一个变量）
target.write(line1)
# 类似   写入函数（换行符）
target.write("\n")
#类似
target.write(line2)
#类似
target.write("\n")
#类似
target.write(line3)
#类似
target.write("\n")


#打印  最后  ，我们 关闭 它
print "And finally, we close it."
#变量target 句号  关闭函数（）
target.close()
