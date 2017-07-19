#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十二题
#列表的定义和循环语句的使用
count=[1,2,3,4,5]
fruits=['apple','oranges','pears']
change=[1,'pennies',2,'dimes',3,'quarters']
#遍历count列表
for num in count:
    print 'the number is %r' %num

#遍历水果
for fruit in fruits:
    print 'the fruit is %s' %fruit

#遍历change
for i in change:
    print i

#列表的添加元素
for ii in range(6,11):
    count.append(ii)
#列表删除最后一个元素
count.pop()
#列表删除一个元素(该元素在列表中):
count.remove(5)
#查看列表元素:
for nums in count:
    print nums
