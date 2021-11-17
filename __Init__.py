# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 这是一个实时把弹幕通过TCP协议传输到UE中的脚本

import time
import Catcher
import Computer
import Sender

# room_id
room_id = 6786164# 21627000

# 设置Host和Port
HOST = '127.0.0.1'
PORT = 8085


class Talker():

    def __init__(self):
        # 创建myDanmu实例
        self.myDanmu = Catcher.Danmu(room_id)
        # 创建Computer实例
        self.myComputer = Computer.Computer()
        # 创建Sender实例
        self.mySender = Sender.Sender(HOST, PORT)

        # 创建danmu与admin
        self.msg_danmu = []
        self.msg_admin = []

    def detect_message(self):
        # 检测所有内容
        _danmus, _admins = self.myDanmu.get_contents()

        # 判断是否有效后加入List
        for _danmu in _danmus:
            self.myComputer.content_danmu.append(_danmu)

        for _admin in _admins:
            self.myComputer.content_admin.append(_admin)

    def solve_message(self):
        # 读取发送的信息
        self.msg_danmu = self.myComputer.get_message_danmu('json_danmu')
        self.msg_admin = self.myComputer.get_message_admin('json_admin')

    def send_message(self):
        # 发送弹幕与管理信息
        if self.msg_danmu:
            self.mySender.send_json(self.msg_danmu)
            # self.mySender.send_danmu(self.msg_danmu)
            # 清除已发送danmu
            self.myComputer.pop_danmu()

        if self.msg_admin:
            self.mySender.send_json(self.msg_admin)
            # 清除已发送admin
            self.myComputer.pop_admin()

    def solve_send(self):
        # 缺一不可
        self.solve_message()
        self.send_message()

    def print_msg_left(self):
        _num = str(len(self.myComputer.content_danmu))
        print("-----" + _num + " Message Left-----")


if __name__ == '__main__':
    print('弹幕机主程序开始运行')

    # 创建一个Talker
    myTalker = Talker()

    while True:
        # 检查与UE4的连接
        _connected = True
        if _connected:
            # 一秒检测一次
            myTalker.detect_message()
            # 解析并发送，0.2秒一次
            myTalker.solve_send()
            time.sleep(0.2)
            myTalker.solve_send()
            # 显示剩余未发送弹幕数量
            myTalker.print_msg_left()
            time.sleep(0.8)
        else:
            time.sleep(1)




