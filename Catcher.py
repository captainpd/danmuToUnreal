import requests
import socket
import threading
import io, sys
import os


class Danmu():

    def __init__(self, rm_id, sv_path='danmu.log', sv_path2='admin.log'):

        # 内存路径
        self.sv_path = sv_path
        self.sv_path2 = sv_path2
        # 弹幕url
        self.url = "https://api.live.bilibili.com/ajax/msg"
        # 请求头
        self.headers = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        }
        # 定义POST传递的参数
        self.data = {
            'roomid': rm_id,
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }
        self.contents_danmu = []
        self.contents_admin = []

        # 声明读写danmu的规则
        self.log_file_write = open(sv_path, mode='a', encoding='utf-8')
        self.log = open(self.sv_path, mode='r', encoding='utf-8').readlines()

        # 声明读写admin的规则
        self.log_file_write2 = open(sv_path2, mode='a', encoding='utf-8')
        self.log2 = open(self.sv_path2, mode='r', encoding='utf-8').readlines()

    def update_danmu(self):
        self.contents_danmu = []
        self.contents_admin = []

        # 获取log文件
        self.log = open(self.sv_path, mode='r', encoding='utf-8').readlines()
        self.log2 = open(self.sv_path2, mode='r', encoding='utf-8').readlines()

        # 获取直播间HTML
        html = requests.post(url=self.url, headers=self.headers, data=self.data).json()

        # 解析观众弹幕
        for content in html['data']['room']:

            # 获取昵称
            nickname = content['nickname']
            # 获取发言
            text = content['text']
            # 获取发言时间
            timeline = content['timeline']
            # 获取类型
            isadmin = content['isadmin']

            msg = timeline + ' ' + nickname + ': ' + text

            if msg + '\n' not in self.log:
                if not isadmin:
                    #  传输Danmu给List
                    self.contents_danmu.append(content)
                    # 记录在本地文件
                    self.log_file_write.write(msg + '\n')
                    self.log_file_write.flush()

        # 解析管理员弹幕
        for content in html['data']['admin']:
            _msg = content['timeline'] + content['nickname'] + content['text']

            if _msg + '\n' not in self.log2:
                # 传输Admin给List
                self.contents_admin.append(content)
                # 记录在本地文件
                self.log_file_write2.write(_msg + '\n')
                self.log_file_write2.flush()

    def get_contents(self):

        # 先更新Contents
        self.update_danmu()
        # 返回contents信息
        return self.contents_danmu, self.contents_admin
