'''
Function:
    网易云音乐自动签到 - Github action 版本
Author:
    Lkhsss
'''
import re
import time
from DecryptLogin import login
from DecryptLogin.modules.core.music163 import Cracker
from configparser import ConfigParser
'''网易云音乐自动签到 - Github action 版本'''
class NeteaseSignin():
    def __init__(self, username, logintype):
        self.username = username
        self.session = self.login()
        self.csrf = re.findall('__csrf=', str(self.session.cookies))[0]
        self.cracker = Cracker()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://music.163.com/discover',
            'Accept': '*/*'
        }

        self.run()
    '''外部调用'''
        
    def run(self):
        # 签到接口
        signin_url = 'https://music.163.com/weapi/point/dailyTask?csrf_token=' + self.csrf
        # 模拟签到(typeid为0代表APP上签到, 为1代表在网页上签到)
        typeids = [0, 1]
        for typeid in typeids:
            client_name = 'Web端' if typeid == 1 else 'APP端'
            # --构造请求获得响应
            data = {
                'type': typeid
            }
            data = self.cracker.get(data)
            response = self.session.post(signin_url, headers=self.headers, data=data)
            response_json = response.json()
            # --判断签到是否成功
            if response_json['code'] == 200:
                self.logging('账号%s在%s签到成功' % (self.username, client_name))
            else:
                self.logging('账号%s在%s签到失败, 原因: %s' % (self.username, client_name, response_json.get('msg')))
    '''模拟登录'''
    def login(self):
        client = login.Client()
        music163 = client.music163(reload_history=True)
        infos_return, session = music163.login(self.username, '', logintype)# pc为短信验证，scanqr为扫描二维码
        return session
    '''logging'''
    def logging(self, msg, tip='INFO'):
        print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} {tip}]: {msg}')
'''读取配置文件'''
config = ConfigParser() # 类实例化
config.read('./config.ini','utf-8')
username = config['user']['username']#读取配置文件
logintype = config['user']['logintype']
NeteaseSignin(username=username, logintype=logintype)