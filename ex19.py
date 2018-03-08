# -*- coding: utf-8 -*-
# 建立函数def  奶酪和饼干 （参数 奶酪数量，饼干盒子）
def cheese_and_crackers(cheese_count, boxes_of_crackers):
     #打印  你 有  整数 奶酪       奶酪数量的参数
	print "You have %d cheeses!" % cheese_count
	#打印  你 有  整数  盒子  饼干          饼干盒子的参数 
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#  打印   男人  这 足够   在 party  (无关功能）
	print "Man that's enough for a party!"
	# 打印  得到 毯子 （无关）  \n   新起一行
	print "Get a blanket. \n"
	

#打印  我们 可以   一双         函数   编写 号码（无关）
print "We can just qive the function numbers directly:"
# 给 函数 奶酪和饼干 的参数 赋值 （20逗号30）
cheese_and_crackers(20, 30)


#打印  我们 可以 使用  变量  从 我们的脚本里
print "OR, we can ues varibles from our script:"
# 定义新变量 amount 奶酪  =10  
amount_of_cheese = 10
#定义 新变量 amount 饼干  =50
amount_of_crackers = 50

#用上面def建立的 奶酪和饼干 函数 调用，等于给函数后面的参数赋值
# 新的变量 amount奶酪 和amount饼干变量
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#打印  我们 可以  把里面 放进 数学题
print "We can even do math inside too:"
# 函数 奶酪和饼干  （两个运算用逗号割开，相当于给函数赋予两个参数）
cheese_and_crackers(10 + 20, 5 + 6)

#打印   我们 可以 把变量和 数学题 结合在一起
print "And we can combine the two, variables and math:"
#函数 奶酪和饼干  （变量+100， 另一个变量+1000） 
#注意 变量在上面赋值过了，是脚本里面的变量，不是函数带的变量
#  函数调用脚本里变量并运算 并不会改动脚本变量的值，只是调用，调用完毕就归还了）
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)