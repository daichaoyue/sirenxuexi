# -*- coding: utf-8 -*- 
# 向下注释
# 汽车=100
cars = 100
# 空间 在 一 车 一辆车的空间 =4 
space_in_a_car = 4.0
# 驾驶员 = 30
drivers = 30
# 乘客 复数=90
passengers = 90
# 车 不 驱动  汽车不开=汽车-驾驶员？？
cars_not_driven = cars - drivers
# 汽车开 =驾驶员
cars_driven = drivers
# 拼车  容量 =“汽车开”乘以“车的空间”
carpool_capacity = cars_driven * space_in_a_car
#平均 乘客        每   车  = “乘客”  除以  汽车开
average_passengers_per_car = passengers / cars_driven


print 'There are', cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."