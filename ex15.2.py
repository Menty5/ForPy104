# -*- coding:utf-8 -*-
# bonus 5
filename = raw_input("Here's your file:")
# Do remenber ""
txt = open(filename)

print txt.read()
# 使用这种方法不用另外输入参数，直接运行再输入，对我来说可以避免遗漏
