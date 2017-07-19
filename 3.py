#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三题
#数字和数学计算
print "多行内容书写:'''内容''' "
print '''
python 中所有的运算符:
1.算术运算符:
+ plus 加号
- minus 减号
/ slash 斜杠
* asterisk 星号
% percent 取余
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
取整除 - 返回商的整数部分,9//2 输出结果 4 , 9.0//2.0 输出结果 4.0

2.比较预算符:
< less-than 小于号
> greater-than 大于号
<= less-than-equal 小于等于号
>= greater-than-equal 大于等于号
==	等于 - 比较对象是否相等	eg:(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	eg:(a != b) 返回 true.
<>	不等于 - 比较两个对象是否不相等	eg:(a <> b) 返回 true。这个运算符类似 !=

3.赋值运算符:
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符 	c += a 等效于 c = c + a
-=	减法赋值运算符 	c -= a 等效于 c = c - a
*=	乘法赋值运算符	    c *= a 等效于 c = c * a
/=	除法赋值运算符  	c /= a 等效于 c = c / a
%=	取模赋值运算符  	c %= a 等效于 c = c % a
**=	幂赋值运算符	    c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a

4.位运算符:
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
eg:(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
eg:(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1
eg:(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
eg:(~a ) 输出结果 -61 ，二进制解释： 1100 0011
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
eg:a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
eg:a >> 2 输出结果 15 ，二进制解释： 0000 1111

5.逻辑运算符:
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
eg:(a and b) 返回 20。
or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
eg:(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
eg:not(a and b) 返回 False

6.成员运算符:
in	    如果在指定的序列中找到值返回 True，否则返回 False。
eg:x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
eg:x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

7.身份运算符
s	    is 是判断两个标识符是不是引用自一个对象
eg:x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象
eg:x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

'''
print 'i will now count my chickens:'
print '母鸡的数量:'
print 'hens:',25.0+30.0/6
print 'roosters:',100.0-25.0*3%4
print 'now i will count eggs:'
print 3+2+1-5+4%2-1.0/4+6
print 'is it true that 3+2<5-7 ?'
print  3+2 < 5-7
print 'what is 3+2',3+2
print 'what is 5-7',5-7
print "oh,that's why it's false"
print "how about some more"
print "is it greater?",5>-2
print 'is it greater or equal?',5>=-2
print 'is it less or equal?',5<=-2
