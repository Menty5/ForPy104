# -*- coding:utf-8 -*-
# bonus 3
def sex(girls, boys):
    print "Our class is a big one"
    print "We have %d girls." % girls
    print "We have %d boys." % boys
    print "That's lovely!\n"
# 1变量
print "measure 1"
sex(15,15)
# 2直接赋值
print "measure 2"
girls = 20
boys = 20

sex(girls, boys)
# 3通过math
print "measure 3"
sex(15 + 15, 15 + 15 )
# 4变量+math
print "measure 4"
sex(girls + 20, boys + 20)
# 4 用户输入
# 记得括号里要有双引号
# print "measure 5"
# girls1 = int(raw_input("girls :"))
# boys1 = int(raw_input("boys :"))

#sex(girls1, boys1)
# 6 用户输入+math
# print "measure 6"
# girls2 = int(raw_input("girls :"))
# boys2 = int(raw_input("boys :"))

# sex(girls2 + 10, boys2 + 10)
# 7用户输入+变量
# print "measure 7"
# girls3 = int(raw_input("girls :"))
# boys3 = int(raw_input("boys :"))
#
# sex(girls + girls3, boys + boys3)
# 8用户输入+变量+math
# print "measure 8"
# girls4 = int(raw_input("girls :"))
# boys4 = int(raw_input("boys :"))
#
# sex(girls + girls4*2 + 10, boys + boys4*2 + 10)
# 9list
# print "measure 9"
# list = [80, 90]
# # 调用list里的所有，在前加*
# # 字符串要用双引号，但这里是整数，不用
# sex(*list)
# 10 list+变量
print "measure 10"
list1 = [90, 100]
sex(girls + list1[0], boys + list1[1])