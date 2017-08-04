# -*- coding:utf-8 -*-
from sys import argv
# 设置参数
script, filename = argv
# 打开文件
txt = open(filename)
# 阅读、打印文件
print "Here's your file %r:" % filename
print txt.read()
# 用户输入文件名、打开文件、打印 ——bonus1
print"Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
# bonus 8
txt.close()
txt_again.close()