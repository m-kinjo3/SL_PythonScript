# file handring example
import os

file=open("/home/mkinjo/Documents/sample.txt",'r')
print('---------------------------')
print(file.readline())
print('---------------------------')
print(file.read())
file.close
