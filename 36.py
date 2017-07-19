#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十六题
#if,循环语句的注意事项

print '编写一个类似于实例35的程序,让其跑起来'

def start():
    print 'you have a diffrent life when you are graduated.'
    choose=['study','work']
    print 'you can choose:'+ choose[0]+'\t'+choose[1]
    next=raw_input("> ")
    if next=='study':
        print 'you will go to study again'
        study()
    elif next=='work':
        print 'you will work now'
        work()
    else:
         print 'you maybe don not choose !'

def study():
    print 'you will choose board or china?'
    next=raw_input(">")
    if next=='china':
        print '你将有一个更高的学历,但是时间会很长'
    elif next=='board':
        print '你将出国深造,你将来会是一个海龟'
        print '你可以去 %s' %['usa','uk','other']
        next=raw_input('>')
        if next=='usa':
            print 'you have make more money'
        elif next=='uk':
            print 'you have good work'
        elif next=='other':
            print '可能比呆在国内好一点'
        else:
            print '也许你是在浪费时光'
    else:
        print '你是在混日子'
def work():
    print 'congratation,you choose work.'
    print 'you can choose blue or white?'
    next=raw_input(">")
    if next=="blue":
        print 'the work is hard.'
    elif next=="white":
        print '你是高收入人群'
    else:
        print '你在默默奉献自己'

start()