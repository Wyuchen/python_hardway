#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第四十二题,游戏重现编写

from sys import  exit
from random import  randint
class Game(object):
    def __init__(self,start):
        self.quips = ['you died, you kinda suck at this,你死了，你有点恶心',
                 'nice job,you died .., jackass.不错，你死了，混蛋。',
                 'such a luser.如此失败',
                 'i have a small puppy that is better at this,你不改如此狂妄自大']
        self.start=start
    def play(self):
        next=self.start
        while True:
            print "\n-----------"
            room=getattr(self,next)#获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，可以在后面添加一对括号
            next=room()

def death(self):
    print self.quips[randint(0,len(self.quips)-1)]
    #randint(0,len(quips)-1)随机获取quips中的某一个元素
    exit(1)

def central_corridor():#中央走廊
    print 'the gothons of planet percal #25 have invaded your ship and destoryed,行星percal # 25 gothons入侵和破坏你的船'
    print 'your entire crew,you are the last surviving member and your last你的全体船员，你是最后一个幸存的成员，也是你的最后一个成员'
    print 'mission is to get the neutron destruct bomb from the weapons armory,任务是从武器库获得中子破坏炸弹，'
    print "put it in the bridge, and blow the ship up after getting into an,把它放在桥上，进入船后把它炸掉"
    print "escape pod.逃生舱"
    print "\n"
    print "You're running down the central corridor to the Weapons Armory when,你正沿着中央走廊跑去武器库这时"
    print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume,一个gothon跳出来，红鳞，黑暗肮脏的牙齿，和邪恶的小丑服装"
    print "flowing around his hate filled body.He's blockingthe door to the 流动在他充满仇恨的身体。他堵门的"
    print "Armory and about to pull a weapon to blast you.军械库，准备用武器来炸你"

    action=raw_input('>')
    if action=='shoot!':#射击
        print "Quick on the draw you yank out your blaster and fire it at the Gothon.快速绘制你拔出你的冲击波和火焰在gothon"
        print "His clown costume is flowing and moving around his body, which throws 他的小丑服装在他的身体周围流动和移动"
        print "off your aim. Your laser hits his costume but misses him entirely. This 偏离目标。你的激光击中他的服装，但完全错过了他。这"
        print "completely ruins his brand new costume his mother bought him, which 完全毁了他妈妈给他买的新衣服"
        print "makes him fly into an insane rage and blast you repeatedly in the face until 让他飞进疯狂的狂怒中，然后不断地在你面前爆炸"
        print "you are dead.Then he eats you. 你死了,然后他吃了你"
        return 'death'
    elif action == "dodge!":#回避
        print "Like a world class boxer you dodge, weave, slip and slide right,像一个世界级拳击手你躲闪，编织，滑和滑的权利"
        print "as the Gothon's blaster cranks a laser past your head.作为gothon的霸曲柄激光过去你的头"
        print "In the middle of your artful dodge your foot slips and you,在你巧妙躲闪的中间，你的脚滑倒了"
        print "bang your head on the metal wall and pass out.把你的头撞在金属墙上，然后昏倒"
        print "You wake up shortly after only to die as the Gothon stomps on,你醒来后不久，只能以死为gothon践踏"
        print "your head and eats you.你被吃了"
        return 'death'
    elif action == "tell a joke":#开玩笑
        print "Lucky for you they made you learn Gothon insult in the academy.你很幸运，他们让你在学校学习侮辱gothon"
        print "You tell the one Gothon joke you know:你告诉一个笑话，你知道gothon"
        print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.那个星球的语言"
        print "The Gothon stops, tries not to laugh, then busts out laughing and can't move. gothon停止，尽量不笑，然后大笑和不能移动"
        print "While he's laughing you run up and shoot him square in the head 当他在笑的时候，你跑上去射他脑袋"
        print "putting him down, then jump through the Weapon Armory door.把他放下，然后从武器库门跳过去"
        return 'laser_weapon_armory'
    else:
        print "DOES NOT COMPUTE!"
        return 'central_corridor'

def laser_weapon_armory():
    print "You do a dive roll into the Weapon Armory, crouch and scan the room,你潜入武器库，蹲下并扫视房间"
    print "for more Gothons that might be hiding.It's dead quiet, too quiet.更多的gothons可能隐藏。它是死的安静，太安静了"
    print "You stand up and run to the far side of the room and find the 你站起来，跑到房间的另一边，找到"
    print "neutron bomb in its container.There's a keypad lock on the box 它的容器里有一个小炸弹，盒子上有一个键盘锁"
    print "and you need the code to get the bomb out.If you get the code 如果你得到了密码，你就需要密码来释放炸弹"
    print "wrong 10 times then the lock closes forever and you can't 错误10次，然后锁永远关闭，你不能"
    print "get the bomb. The code is 3 digits.得到炸弹。密码是3位数字。"
    code='%d%d%d'%(randint(1,9),randint(0,9),randint(0,9))
    print code
    guess=raw_input("[keypad]>")
    guesses=0
    #判断密码是否匹配并且只有10次机会去猜测
    while guess!=code and guesses<10:
        print 'ERROR CODE'
        guesses+=1
        guess=raw_input("[keypad]>")
    if guess==code:
        print "The container clicks open and the seal breaks,letting gas out.容器点击打开，密封破裂，让气体排出"
        print "You grab the neutron bomb and run as fast as you can to the 你抓起中子弹，尽可能快地跑到"
        print "bridge where you must place it in the right spot.你必须把它放在正确位置的桥"
        return 'the_bridge'
    else:
        print "The lock buzzes one last time and then you hear a sickening 锁里最后一次，然后你听到一个令人作呕的"
        print "melting sound as the mechanism is fused together.熔化的声音，因为机制融合在一起"
        print "You decide to sit there, and finally the Gothons blow up the你坐在那里，最后gothons炸毁"
        print "ship from their ship and you die.从他们的船上航行，你就死了"
        return 'death'

def the_bridge():
    print "You burst onto the Bridge with the neutron destruct bomb 你拿着破坏炸弹冲进了桥上"
    print "under your arm and surprise 5 Gothons who are trying to你正在准备行动的时候,惊讶的发现有5 个Gothons尝试着"
    print "take control of the ship. Each of them has an even uglier 控制船。他们每个人都有一个更丑的"
    print "clown costume than the last.They haven't pulled their 小丑服装比最后一件，他们没有拉他们的"
    print "weapons out yet, as they see the active bomb under your 武器还没出来，因为他们看到你下面的有源炸弹"
    print "arm and don't want to set it off.手臂，不想把它关掉。"
    action=raw_input(">")
    if action == "throw the bomb":#仍炸弹
        print "In a panic you throw the bomb at the group of Gothons 在一片恐慌你扔炸弹在gothons组"
        print "and make a leap for the door.Right as you drop it a 向门口跳一跳，当你掉下来的时候"
        print "Gothon shoots you right in the back killing  you. Gothon射中了你"
        print "As you die you see another Gothon frantically try to disarm 当你死了你看到另一个gothon拼命试图解除"
        print "the bomb. You die knowing they will probably blow up when 炸弹。你知道他们可能会在什么时候爆炸"
        print "it goes off. 它熄灭"
        return 'death'
    elif action == "slowly place the bomb":#慢慢放置炸弹
        print "You point your blaster at the bomb under your arm 你用枪瞄准你胳膊下的炸弹"
        print "and the Gothons put their hands up and start to sweat. 并且Gothons把他们的双手开始出汗"
        print "You inch backward to the door, open it, and then carefully 你向后一寸地向门口走去，打开门，然后小心地走"
        print "place the bomb on the floor, pointing your blaster at it.把炸弹放在地板上，指着你的爆破手。"
        print "You then jump back through the door, punch theclose button"
        print "and blast the lock so the Gothons can't get out.爆锁，gothons不能出去"
        print "Now that the bomb is placed you run to the escape pod to既然炸弹已经放好了，你就逃到逃生舱去了"
        print "get off this tin can.把这罐头罐取下来"
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE!"
        return "the_bridge"

def escape_pod():
    print "You rush through the ship desperately trying to make it to你拼命地穿过船，试图把它弄到"
    print "the escape pod before the whole ship explodes. It seems like 整个飞船爆炸前的逃生舱。它看起来像"
    print "hardly any Gothons are on the ship, so your run is clear of几乎没有任何gothons正在船上，所以你的运行是明确的"
    print "interference.You get to the chamber with the escape pods, and 干扰。你用逃生舱进入房间，然后"
    print "now need to pick one to take.Some of them could be damaged 现在需要挑选一个，其中一些可能会被损坏。"
    print "but you don't have time to look.There's 5 pods,which one?但是你没有时间看，有5个分离仓，哪一个？"
    good_pod = randint(1,5)
    guess = raw_input("[pod #]> ")
    if int(guess) != good_pod:
        print "你进入了 %s 救生舱 and hit the eject button.点击发射按钮" % guess
        print "The pod escapes out into the void of space,then吊舱逃逸到太空的空隙，然后"
        print "implodes as the hull ruptures, crushing your body 时船体断裂，粉碎你的身体"
        print "into jam jelly. 粉碎"
        return 'death'
    else:
        print "你进入了 %s 救生舱 and hit the eject button.点击发射按钮" % guess
        print "The pod easily slides out into space heading to,分离仓很容易滑入太空"
        print "the planet below. As it flies to the planet, you look下面的行星。当它飞到地球时，你看"
        print "back and see your ship implode then explode like a 看看你的船爆炸然后爆炸似的"
        print "bright star, taking out the Gothon ship at the same 明亮的星，取出gothon船同时"
        print "time.You won!你赢了"
        exit(0)

ROOMS = {
'death': death,
'central_corridor': central_corridor,
'laser_weapon_armory': laser_weapon_armory,
'the_bridge': the_bridge,
'escape_pod': escape_pod
}

a_game=Game('central_corridor')
a_game.play()














