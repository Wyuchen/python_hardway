#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第十九题
def chese_and_crackers(cheese_count,boxes_of_crackers):
    print 'you have %d cheeses!' % cheese_count
    print 'you have %d boxes of crackers!' % boxes_of_crackers
    print "man that is enough for a party"
    print 'get a blanket!'

print '第一种方法----->we can just give the function numbers directly:'

chese_and_crackers(20,30)

print '第二种方法---->or,we can use variable from our script:'
amount_of_cheese=10
amount_of_crackers=50
chese_and_crackers(amount_of_cheese,amount_of_crackers)

print '第三种方法---->we can even do math inside too:'
chese_and_crackers(10+20,5+6)

print '第四种方法---->we can combine the two,variables and math:'
chese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
