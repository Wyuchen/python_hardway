#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十二题
#raw_put的提示输入
age=raw_input("please input your ages:")
print 'age 的类型为:',type(age)
age1=int(raw_input("please input your ages:"))
print 'age1 的类型为:',type(age1)

height=raw_input("please input your tall:")
print '使用age和heignt:'
print 'you are %s years old,you are %s tall' % (age,height)
print '使用age1和heignt:'
print 'you are %d years old,you are %s tall' % (age1,height)