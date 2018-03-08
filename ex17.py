# -*- coding: utf-8 -*-
#从 sys模块 导入 argv
from sys import argv
#从os.path模块（文件属性获取模块） 导入 exists
# 存在，  将文件名字符做为参数，如果存在返回True 否则False
from os.path import exists

#解包变量 脚本  from_file to_file =argv
script, from_file, to_file = argv

# 打印 从%s 复制到%s   带入后面变量
print "Copying from %s to %s" % (from_file, to_file)

#我们将这两行 写成一行
#We could do these two on one line too, how?
# 定义变量in_file =打开 from_file返回的值
in_file = open(from_file)
#定义变量 indata  =  上个变量读取的值
indata = in_file.read()

#打印 这输入 的文件 是%d(整数） 长整数 %带入后面 len（）以整数形式返回字符串长度
print "The input file is %d bytes long" % len(indata)

#打印  与功能无关
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#定义变量 out_file =打开 to_file返回的值，并用 写入模式打开
out_file = open(to_file, 'w')
# 上面打开to_file的值  句号 写入函数（indata）写进indata这个参数里
out_file.write(indata)

print "Alright, all done."
#两个文件各自 用close（）关闭函数关闭
out_file.close()
in_file.close()
