#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十九题
#列表的操作
ten_thing='a b c d e f g h'
print 'wait,there are not 10 thing in that list,let us fix that'

suff=ten_thing.split(' ')
more_stuff=["day",'night','song','frisbee','cron','banana','gril','boy']
while len(suff)!=10:
    next_one=more_stuff.pop()
    print 'adding: ',next_one
    suff.append(next_one)
    print 'there are %d items now.' %len(suff)

print 'there we go: ',suff
print 'let us do some things with suff'

print suff[1]              #查看下标为1的元素
print suff[-1]             #查看最后一个元素
print suff.pop()           #移除最后一个元素,并打印出最后一个元素
print ' '.join(suff)       #查看suff并且以' '分隔
print '#'.join(suff[3:5])  #切片处理并且以#好分隔

print '''
关于函数的方法的细节认识:
>>> class Thing(object):
...     def test(hi):
...         print "hi"
...
>>> a = Thing()
>>> a.test("hello")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given)

报错:test()只可以接受 1 个参数,实际上给了两个.它意味着 python 把 a.test("hello") 改成
了 test(a, "hello"),而有人弄错了,没有为它添加 a 这个参数.

改为: def test(self,hi):
         print hi
'''
