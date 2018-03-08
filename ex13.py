# -*- coding: utf-8 -*-
#从 sys （from sys 从内置模块，固定用法 不可更改名称） 
#  导入 argv模块（保存运行脚本时输入的参数，参数变量）
from sys import argv     

#变量导出命名 脚本 第一 第二 第三  = argv  （命名可以随意）
#将 argv的参数 赋予左边的变量中
script, first, second, third, deqwas = argv

# script 变量相当于  argv[0] 也就是脚本自己的名字
print "The script is called:", script
print "Your first variable is:", first, 
print "Your second variable is:", second
print "Your third variable is:", third
print "sad", deqwas
