#!/usr/bin/python
# -*- coding: UTF-8 -*-

from wxpy import *
import lunch
# import pytesseract
# from PIL import Image
bot = Bot(cache_path=True,console_qr=False)

# 机器人账号自身
myself = bot.self
tuling = Tuling(api_key='56b8d10e47c24affb7fc519cf8591fd7')
my_group = bot.groups().search(u'锡东心诚')[0]
lunchSystem = lunch.Lunch()


txt = '开始订餐啦'
my_group.send(txt)
# my_group.send(txt.encode('utf-8'))
@bot.register([my_group])
def forward_boss_message(msg):
    if msg.type == 'Text':
        print(msg.member.name)
        index = msg.text.find('#')
        if index > -1:
            dc(msg)
            return

    elif msg.type == 'Picture':
        print('接受到图片')
        # msg.reply(u'还不会斗图')
        # msg.get_file('./'+msg.file_name)
        # image = Image.open('./'+msg.file_name)
        # code = pytesseract.image_to_string(image)
        # print code

def send(msg):
    my_friend.send(msg)

def showRule():
    txt = '订餐系统 v0.0.1\n'
    txt += '1 订餐输入add# + 你要的套餐(add#卤肉饭+椒盐鸡腿),更新操作与此相同\n'
    txt += '2 取消订餐输入cancel#\n'
    txt += '3 获取订餐列表输入menu#\n'
    txt += '4 获取订单消息信息输入detail#\n'
    txt += '有bug请@我\n'
    txt += '祝使用愉快！'
    my_group.send(txt)



def dc(msg):
    index = msg.text.find('#')
    rmsg = None
    if index > -1:
        command = msg.text[:index].strip()
        content = msg.text[index+1:].strip()
        if command == 'add' or command == 'update':
            rmsg = lunchSystem.updateList(msg.member.name,content)
        elif command == 'cancel':
            rmsg = lunchSystem.delList(msg.member.name)
        elif command == 'menu':
            rmsg = lunchSystem.getResult()
        elif command == 'detail':
            rmsg = lunchSystem.getList()
    if rmsg:
        msg.reply(rmsg)

def getSignature():
    list = bot.friends()
    for friend in list:
        print(friend.name,friend.signature)


def getGroupSignature(group):
    for member in group:
        print(member.name,member.signature)

getGroupSignature(my_group)
# 堵塞线程
embed()
