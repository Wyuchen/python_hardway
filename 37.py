#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十七题
#复习所有的字符(实例3中已经列出一部分)

print '''
关键字
1.逻辑预算符: and  or not
2.模块的引用:from   import   as(别名)
3.循环语句: for  while
4.条件判断: if  elif  else  break continue pass
5.异常处理: try finally raise execpt
6.匿名函数: lambda ---->lambda x:x+1
7.删除:del
8.函数相关:def return  class
9.成员判断: is  in
10打印:exec  print

11.yield:类似于return,告诉程序，要求函数返回一个生成器
def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

12.assert:断言，这个关键字用来在运行中检查程序的正确性，和很多其他语言是一样的作用:
---->assert len(mylist) >= 1

13.with
它实质是一个控制流语句，with可以用来简化try-finally语句。它的主要用法是实现一个类__enter__（）和__exit__()方法
class controlled_execution:
    def _enter__(self):
        set things up
        return thing
    def __exit__(self, type, value,  traceback):
        tear thing down
with controlled_execution() as thing:
    some code

14.global: 定义全局变量


字符转义:
1."\\"---->\
2."\'" ---->'
3."\"" ---->"
4."\a" ---->响铃
5."\b" ---->退格(Backspace)
6."\f" ---->换页
7."\n" ---->换行
8."\r" ---->回车
9."\t" ---->tab
10."\v"---->纵向制表符

格式化输出:
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    无符号整数(十六进制)
%X    无符号整数(十六进制大写字符)
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"

操作符号:
 +(加)    -(减)    *(乘)   *(幂)   /(除)    //(商)    %(取余)

 <(小于)  >(大于)   <=(小于等于)    >=(大于等于)  ==(等于)  !=(不等于)<>

  ( ) (小括号)   [ ] (中括号)   { }(大括号)

 @   ,(逗号)   :(冒号)    .(点)   =(赋值)   ;(分号)

 +=(加等于)   -=(减等于)    *=(乘等于)   /=(除等于)   //=(商等于)   %=(取余等于)

 **=(幂等于)
'''