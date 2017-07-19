#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第十八题
#命名,变量,代码,函数
#函数
def print_two(*args):
    arg1,arg2=args
    print 'arg1: %r,arg2:%r' %(arg1,arg2)
#跳过整个参数解包的过程,直接使用 () 里边的名称作为变量名
def again_print_two(arg1,arg2):
    print "arg1=%r,arg2=%r" %(arg1,arg2)
# 函数如何接受单个参数
def print_arg1(arg1):
    print 'arg1:',str(arg1)
#函数可以不接收任何参数
def print_noth():
    print 'nothing'

print_two(1,2)
print_arg1(560)
again_print_two('wang','zhen')