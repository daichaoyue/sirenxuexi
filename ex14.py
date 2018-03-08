# -*- coding: utf-8 -*-
#从内置模块 中 导入 参数变量
from sys import argv

# 把变量scrigt user_name 变量从 参数变量里面解压到文件里
script, user_name  = argv
#定义变量 prompt = 提示符（根据需要可变）
prompt = '{}{} '

#打印 使用了两个%s  带入后面的变量
print "Hi %s, I'm the %s script." % (user_name, script)
#打印 
print "I'd like to ask you a few questions."
#打印 %s 带入后面变量
print "Do you like me %s?" % user_name
#定义变量 likes = 获取用户输入函数，并在括号里使用prompt变量
likes = raw_input(prompt)

#类似上面
print "Where do you live %s?" %user_name
lives = raw_input(prompt)

#类似上面
print "What kind of computer do you have?"
computer = raw_input(prompt)

#打印 多行字符串，带了三个%r   。语句结束直接跟三个 变量（上面获取用户输入的变量）
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)