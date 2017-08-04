# bonus 2
from sys import argv

script, filename = argv

file = open('test.txt')

print file.read()

file.close()