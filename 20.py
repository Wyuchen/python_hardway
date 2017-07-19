#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第二十题
#函数和文件结合
from sys import argv
script,file=argv
#读取文件内容
def read(f):
    print f.read()
#指针回到开头
def rewind(f):
    f.seek(0,0)
#读取一行文件内容
def read_a_line(line_count,f):
    print line_count,f.readline()
#关闭文件
def close(f):
    f.close()

current_file=open(file)
print 'read all file:'
read(current_file)

print '指针回到开头完成!'
rewind(current_file)

current_line=1
print '打印出一行的内容:'
read_a_line(current_line,current_file)
print '打印出二行的内容:'
current_line+=1
read_a_line(current_line,current_file)
print '打印出三行的内容:'
current_line+=1
read_a_line(current_line,current_file)

print '关闭文件'
close(current_file)

