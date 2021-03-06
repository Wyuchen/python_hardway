#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第四十四题
#函数,类,代码风格,注释
print '''
函数的风格
1)由于各种各样的原因,程序员将 class (类)里边的函数称作 method (方法)。
很大程度上这只是个市场策略(用来推销 OOP),不过如果你把它们称作“函数”的话,是会有啰嗦的人跳出来纠正你的。
2)在你使用 class 的过程中,很大一部分时间是告诉你的 class 如何“做事情”。
给这些函数命名的时候,与其命名成一个名词,不如命名为一个动词,作为给 class 的一个命令。
就和 list 的 pop (抛出)函数一样,它相当于说:“嘿,列表,把这东西给我 pop 出去。”
它的名字不是 remove_from_end_of_list ,因为即使它的功能的确是这样,这一串字符也不是一个命令。
3)函数保持简单小巧。

类的风格:
1)你的 class 应该使用 “camel case(驼峰式大小写)”,例如你应该使用
SuperGoldFactory 而不是 super_gold_factory。
2) __init__ 不应该做太多的事情,这会让 class 变得难以使用。
3)你的其它函数应该使用 “underscore format(下划线隔词)”,所以你可以写my_awesome_hair,而不是 myawesomehair 或者 MyAwesomeHair 。
3)用一致的方式组织函数的参数。如果你的 class 需要处理 users、dogs、
和cats,就保持这个次序(特别情况除外)。如果一个函数的参数是(dog, cat, user) ,另一个的是 (user, cat, dog) ,这会让函数使用起来很困难。
4)不要对全局变量或者来自模组的变量进行重定义或者赋值,让这些东西自顾自就行了。
5)不要一根筋式地维持风格一致性,这是思维力底下的妖怪喽啰做的事情。一致性是好事情,不过愚蠢地跟着别人遵从一些白痴口号是错误的行为
6)永远永远都使用 class Name(object) 的方式定义 class,否则你会碰到大麻烦。

代码风格:
1)学着模仿别人的风格写 Python 程序,直到哪天你找到你自己的风格为止
2)一旦你有了自己的风格,也别把它太当回事。程序员工作的一部分就是和别人的代码打交道,有的人审美就是很差。相信我,你的审美某一方面一定也很差,只是你从未意识到而已
3)如果你发现有人写的代码风格你很喜欢,那就模仿他们的风格
4)为了以方便他人阅读,为自己的代码字符之间留下一些空白。你将会看到一些很差的程序员,他们写的代码还算通顺,但字符之间没有任何空间。这种风格在任何编
程语言中都是坏习惯,人的眼睛和大脑会通过空白和垂直对齐的位置来扫描和区隔视觉元素,如果你的代码里没有任何空白,这相当于为你的代码上了迷彩装。如果
一段代码你无法朗读出来,那么这段代码的可读性可能就有问题。如你找不到让某个东西易用的方法,试着也朗读出来。这样不仅会逼迫你慢速而且真正仔细阅读过
去,还会帮你找到难读的段落,从而知道那些代码的易读性需要作出改进

好的注释:
1)有程序员会告诉你,说你的代码需要有足够的可读性,这样你就无需写注释了。他们会以自己接近官腔的声音说“所以你永远都不应该写代码注释。”这些人要么是一
些顾问型的人物,如果别人无法使用他们的代码,就会付更多钱给他们让他们解决问题。要么他们能力不足,从来没有跟别人合作过。别理会这些人,好好写你的注解
2)写注解的时候,描述清楚为什么你要这样做。代码只会告诉你“这样实现”,而不会告诉你“为什么要这样实现”,而后者比前者更重要
3)当你为函数写文档注解的时候,记得为别的代码使用者也写些东西。你不需要狂写一大堆,但一两句话谢谢这个函数的用法还是很有用的
4)最后要说的是,虽然注解是好东西,太多的注解就不见得是了。而且注解也是需要维护的,你要尽量让注解短小精悍一语中的,如果你对代码做了更改,记得检查并
更新相关的注解,确认它们还是正确的
'''