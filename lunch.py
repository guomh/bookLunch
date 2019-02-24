#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Lunch():
    def __init__(self):
        self.list = {}

    def updateList(self,user,content):
        user = user.encode('UTF-8')
        content = content.encode('UTF-8')
        if(self.list.get(user)):
            return self.changeList(user,content)
        else:
            return self.addList(user,content)

    def addList(self,user,content):
        self.list[user] = content
        return user + ' 订餐成功，内容为: '+content

    def changeList(self,user,content):
        old = self.list[user]
        self.list[user] = content
        return user + ' 已将： '+old+' 改为：'+content

    def delList(self,user):
        user = user.encode('UTF-8')
        del self.list[user]
        return user +' 已取消订餐'

    def getList(self):
        obj = self.list
        msg = ''
        for a in obj:
            msg += a +':'+obj[a]+'\n'
        return msg

    def getResult(self):
        result = ''
        tmp = {}
        for i in self.list:
            list =  self.list[i].split('+')
            for a in range(len(list)):
                if tmp.get(list[a]):
                    tmp[list[a]] += 1
                else:
                    tmp[list[a]] = 1
        for i in tmp:
            result += i+'x'+str(tmp[i])+'  '
        return result

if __name__ == '__main__':
    lunch = Lunch()
    print(lunch.updateList('a','111'))
    print(lunch.updateList(u'过明辉',u'尖椒鸡套餐'))
    print(lunch.updateList('c','333'))
    print(lunch.getList())
    print(lunch.getResult())
