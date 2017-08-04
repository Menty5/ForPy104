# -*- coding:utf-8 -*-
from sys import argv

script, input_file = argv
# 定义函数print_all，调用时，打印f文件中的内容
def print_all(f):
    print f.read()
# seek：移动文件读取指针到指定位置，默认从0（开头）开始，对当前位置进行操作（所以下文的1才会出现在开头）
def rewind(f):
    f.seek(0)
# 每次调用print_a_line函数上，打印current_line的值，和逐行阅读文件的值
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print"Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)