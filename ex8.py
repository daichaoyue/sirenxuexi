# -*- coding: utf-8 -*-
#向下注释
# 定义变量formatter（简写for）  = 四个原始语言显示的 格式化字符
formatter = "%r %r %r %r"

#打印 for 等于%r 1  %r 2 %r 3 % 4
print formatter % (1, 2, 3, 4)
#打印 for 等于%r one %r two %r three %r four
print formatter % ("one", "two", "three", "four")
#打印 for 等于%r 真 %r 假 %r 假 %r 真
print formatter % (True, False, False, True)
#打印 for 等于 %r 变量for的定义 四个%r，四个%r 四个%r 四个%r
print formatter % (formatter, formatter, formatter, formatter)
#打印 for 等于 每句话都跟着，这是一个长字符，每个%r 跟着一句话，
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"Sut it didn't sing.",
	"So I said goodnight."
)
