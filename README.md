## 一个简单的，基于Github Action的网易云自动签到脚本
> 为了需要做了个网易云签到脚本。配置好后可以一直不用管。不用自备服务器，没有其他花里胡哨功能。

> 本人学术不精，同时也暂时没有时间改良登录配置，将就一下吧


### Github Actions 部署指南
运行环境：windows 11
python: 3.9.5
运行库：DecryptLogin
#### 一、克隆此项目到本地
1.可以点击**下载**按钮下载zip包
![下载zip包](./%E6%95%99%E7%A8%8B%E5%9B%BE%E7%89%87/%E4%B8%8B%E8%BD%BDzip%E5%8C%85.png)
2.也可以复制此代码到cmd运行↓
`git clone Lkhsss/163music-autocheckin`
#### 二、配置配置文件
在`config.ini`文件中配置自己的设置
`username`为你的网易云账号电话号码
`logintype`为登录方式（`pc`、`scanqr`可选，一个是验证码登录，一个是扫描二维码登录）
#### 三、获得`music163.pkl`文件
克隆到本地后，导航到此文件夹，使用`pip install -r requirements.txt`安装运行库
然后运行
