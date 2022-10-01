#coding=utf-8

import os
import re

command = 'pip show DecryptLogin' #可以直接在命令行中执行的命令

r = os.popen(command) #执行该命令

info = r.readlines()  #读取命令行的输出到一个list

print(info[7])
path = str(re.sub("\n", "", (re.sub("Location: ", "", info[7])))) + '\DecryptLogin\modules\clients\music163.pkl'
print(path)

os.system('copy ' + path + ' ' + './')
print("\n运行出错解决方案：")
print("解决方案一：重新运行main.py并再次尝试")
print("解决方案二：在python根目录寻找  \lib\site-packages\DecryptLogin\modules\clients\music163.pkl 文件，并将其复制到本目录下")
print("解决方案三：查看DecryptLogin库是否已安装，可以使用命令\"pip show DecryptLogin\"查看，查看安装路径也是这个命令")
print("如还无法解决，截图发issue给我")