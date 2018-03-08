# -*- coding: utf-8 -*-
#这是一个你喜欢的脚本 参数
#This one is like your scripts with argv
#函数建立固定格式 def 函数名（）：    然后下行缩进
# *args  等于把所有的参数放在 args的列表里
def print_two(*args):
#   从列表args解包 arg1和arg2
    arg1, arg2 = args
	#打印 rag1 arg2 用%r 方式显示， 后面带入%（arg1 arg2）
	#注意这时候缩进还没结束，说明这属于函数内容
    print "arg1: %r,  arg2: %r" %(arg1, arg2)

# ok  这个 *args  实际上     无意义    我们只要这样做就是
# ok ,that *args is actually piintless, we can just do this
# 建立函数 def  函数名（arg1,arg2)两个参数  ：
def print_two_again(arg1, arg2):
    #打印   参数1  参数2   用%r 方式显示
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# 这仅     需要  一个 参数
#this just takes one argument
# 建立函数 def 函数名（arg1）参数   ：
def print_one(arg1):
#打印 参数1  %r 
    print "arg1: %r" % arg1

# 这个     不需要   参数 	
# this one takes no argument
#建立函数 def 函数名（） 没有参数 ：
def print_none():
#打印 我什么也没有
    print "I got nothin'."
	
#下面四行 直接使用函数，等同于迷你脚本，不需要print之类的语法	
#  使用函数的时候  括号里需要把参数带上，用逗号割开
print_two("Zed","Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


