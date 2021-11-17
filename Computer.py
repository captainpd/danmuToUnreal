import json


class Computer:

    def __init__(self):
        self.content_danmu = []
        self.content_admin = []

    def get_message_danmu(self, mode):

        if self.content_danmu:
            # _danmu 为列表中存储的第一个弹幕
            _danmu = self.content_danmu[0]
            if mode == 'json_danmu':
                # 获取所有信息
                _type = 'danmu'
                _text = self.get_text(_danmu)
                _nickname = self.get_nickname(_danmu)
                j = {"type": _type, "nickname": _nickname, "text": _text}
                # 将Json转化为二进制
                _msg = json.dumps(j, ensure_ascii=False)
                print('(Danmu)' + _msg)
                return _msg

    def get_message_admin(self, mode):

        if self.content_admin:
            # _admin 为列表中存储的第一个管理员信息
            _admin = self.content_admin[0]
            if mode == 'json_admin':
                # 获取所有信息
                _type = 'admin'
                _text = self.get_text(_admin)
                # 计算名字和礼物
                _gift = self.get_gift(_text)
                _nickname = self.get_gift_sender(_text)
                j = {"type": _type, "nickname": _nickname, "gift": _gift}
                # 将Json转化为二进制
                _msg = json.dumps(j, ensure_ascii=False)
                print('(Admin)' + _msg)
                return _msg

    def get_text(self, content):
        return str(content['text'])

    def get_nickname(self, content):
        return content['nickname']

    def get_uid(self, content):
        return content['uid']

    def pop_danmu(self):
        self.content_danmu.pop(0)

    def pop_admin(self):
        self.content_admin.pop(0)

    def get_gift_sender(self,text):
        start = text.find('谢谢') + 2  # 由于读到的是str的最后一个的位置，因此要加上字符长度
        end = text.find('赠送滴')

        sender = str(text[start:end])
        return sender

    def get_gift(self, text):
        start = text.find('赠送滴') + 3  # 由于读到的是str的最后一个的位置，因此要加上字符长度
        end = text.find('~~~')

        gift = str(text[start:end])
        return gift

    # 'text'——str——弹幕
    # 'nickname'——str——昵称
    # 'uid'——int——用户id
    # 'timeline'——str——时间
    # 'dm_type'——int——弹幕类型
    # ‘guard_level’——int——守护等级
    # ‘medel[00]’——int——粉丝牌等级
    # ‘medel[02]’——int——粉丝牌主播名称
