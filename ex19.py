# -*- coding:utf-8 -*-
# 定义函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# 1直接给参数赋值
print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)

# 2在脚本给参数赋值
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# 先赋值，再代入
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 3使用运算赋值
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 4将变量和数字联系起来赋值
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
