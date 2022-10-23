"""
Function:
    网易云音乐自动签到 - Github action 版本
Author:
    Lkhsss
"""

import re
from DecryptLogin import login
from DecryptLogin.modules.core.music163 import Cracker
from configparser import ConfigParser

import os
from datetime import datetime, timedelta, timezone
import logging

"""网易云音乐自动签到 - Github action 版本"""

class NeteaseSignin:
    def __init__(self):
        self.setting()

        self.logs = self.log_setting()

        self.session = self.login()
        self.csrf = re.findall("__csrf=", str(self.session.cookies))[0]
        self.cracker = Cracker()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "http://music.163.com/discover",
            "Accept": "*/*",
        }

        self.run()

    """外部调用"""

    def setting(self):
        config = ConfigParser()  # 类实例化
        config.read("./config.cfg", "utf-8")
        self.username = config["user"]["username"]  # 读取配置文件
        self.logintype = config["user"]["logintype"]  # 读取配置文件
        self.log_status = config["log"]["logs"]  # 读取配置文件
        self.log_path = config["log"]["dirpath"]  # 读取配置文件

    def log_setting(self):

        log_path = self.log_path  # 全局变量转局部变量

        if os.path.exists(log_path):
            pass
        elif not os.path.exists(log_path):
            os.makedirs(log_path)
            print("创建文件夹")
        else:
            print("检查日志文件夹错误")

        logger = logging.getLogger("ACI")  # Auto check in 简称 ACI

        logger.setLevel(logging.INFO)  # 设置为INFO级别

        format = logging.Formatter("[%(asctime)s] [%(levelname)s]: %(message)s")  # 模板

        # 标准流处理器，设置的级别为INFO
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(format)
        logger.addHandler(stream_handler)

        # 文件处理器，设置的级别为INFO
        filename = str(self.log_path) + "/" + str(self.getBeijinTime()) + ".log"
        file_handler = logging.FileHandler(filename=filename, encoding="utf_8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(format)
        logger.addHandler(file_handler)

        return logger

    def getBeijinTime(self):
        """
        获取北京时间的日期
        """
        try:
            SHA_TZ = timezone(timedelta(hours=8), name="Asia/Shanghai")
            utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
            beijing_now = utc_now.astimezone(SHA_TZ)
            return beijing_now.date()
        except:
            return None

    def run(self):
        # 签到接口
        signin_url = (
            "https://music.163.com/weapi/point/dailyTask?csrf_token=" + self.csrf
        )
        # 模拟签到(typeid为0代表APP上签到, 为1代表在网页上签到)
        typeids = [1]
        for typeid in typeids:
            client_name = "Web端" if typeid == 1 else "APP端"
            # --构造请求获得响应
            data = {"type": typeid}
            data = self.cracker.get(data)
            response = self.session.post(signin_url, headers=self.headers, data=data)
            response_json = response.json()
            # --判断签到是否成功
            if response_json["code"] == 200:
                self.logs.info("账号%s在%s签到成功" % (self.username, client_name))
            else:
                if response_json.get("msg") == "重复签到":
                    self.logs.warn(
                        "账号%s在%s签到失败, 原因: %s"
                        % (self.username, client_name, response_json.get("msg"))
                    )
                else:
                    self.logs.error(
                        "账号%s在%s签到失败, 原因: %s"
                        % (self.username, client_name, response_json.get("msg"))
                    )

    def login(self):
        """模拟登录"""
        client = login.Client()
        music163 = client.music163(reload_history=True)
        infos_return, session = music163.login(
            self.username, "", self.logintype
        )  # pc为短信验证，scanqr为扫描二维码
        self.logs.info("尝试使用 [" + self.logintype + "] 方法登录，用户：" + self.username)
        return session

NeteaseSignin()
