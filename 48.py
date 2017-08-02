#/usr/bin/python
#encoding=utf8
#笨方法学python-第四十八题
#目的:编辑出一个能够扫描出用户输入的字,并标注是那种类型的程序

#定义初始化的数据:
Direction=['Direction','north','south','east','west']
Verb=['Verb','go','stop','kill','eat']
Adjective=['Adjective','the','in','of','from','at','it']
Noun=['Noun','door','bear','pricess','cabine']
print '用户可以输入的词有:'
print Direction[1:-1]
print Verb[1:-1]
print Adjective[1:-1]
print Noun[1:-1]
#收集用户输入的命令
stuff=raw_input(">")
#将用户的命令分割(按照空格符进行分割)
words=stuff.split()
#定义一个列表存放这些单词
scentence=[]
#遍历用户给出的单词的意思:
for word in words:
    for date in (Direction,Verb,Adjective,Noun):
        if word  in date:
            scentence.append((date[0], word))
        else:
            continue

print "扫描结果:"
print scentence

