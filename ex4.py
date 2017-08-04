# -*- coding:utf-8 -*-
# 变量cars
cars = 100
# 变量space_in_a_car
space_in_a_car = 4
# 变量drivers
drivers = 30
# 变量passengers
passengers = 90
# 变量cars_not_driven
cars_not_driven = cars - drivers
# 变量cars_driven
cars_driven = drivers
# 变量carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# 变量average_passengers_per_car = passengers / cars_driven
average_passengers_per_car = passengers / cars_driven

print"There are", cars,"cars available."
print"There are only", drivers,"drivers available."
print"There will be", cars_not_driven,"empty cars today."
print"We can transport", carpool_capacity,"people today."
print"We have", passengers,"to carpool today."
print"We need to put about", average_passengers_per_car,"in each car."

# bonus0:定义的变量没有出现car_pool_capacity，也就是说以此为名的变量没有被定义
# bonus1:这里是乘法，如果只用4的话也没什么问题
# bonus2:浮点数指计算机中带有小数的数值
# bonus3：如上
# bonus6:

x = 12345.0
y = 345
print "x/y=",x/y