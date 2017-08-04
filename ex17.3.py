# -*- coding:utf-8 -*-
# bonus 3
file = open('test.txt','r')
new = open('new-file.txt','w')

word = file.read()
new.write(word)

file.close()
new.close()

# bonus 6 :close是为了释放资源