#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第八题
#格式化输出,注意理解%r的作用,能够输出所有的值
print '输出的格式:'
formatter="%r %r %r %r"
print formatter
print formatter % (1,2,3,4)
print formatter % ('one','two','three','four')
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "i had this thing",
    "that you could type up right",
    "but it did't sing",
    "so i said goodnight."
)