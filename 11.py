#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十一题
#从终端获取输入的值
print  '在每行 print 后面加了个逗号,这样的话print就不会输出新行符而结束这一行跑到下一行去了.'
print 'how old are you?',
age=raw_input()
print  'how tall are you?',
height=raw_input()
print 'you are %s old,%s tall' %(age,height)
