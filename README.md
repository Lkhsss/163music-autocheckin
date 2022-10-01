## 一个简单的，基于Github Action的网易云自动签到脚本
> 为了需要把[Charles的皮卡丘](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw)的代码改了一下，做了个可以用github action的网易云签到脚本。配置好后可以一直不用管。不用自备服务器，没有其他花里胡哨功能。

> 本人学术不精，同时也暂时没有时间改良登录配置，将就一下吧


### Github Actions 部署指南
运行环境：windows 11
python: 3.9.5
运行库：DecryptLogin

#### 一、克隆此项目到本地
1.可以点击**下载**按钮下载zip包
<img src="./%E6%95%99%E7%A8%8B%E5%9B%BE%E7%89%87/%E4%B8%8B%E8%BD%BDzip%E5%8C%85.png" alt="下载ZIP包" width="60%">
2.也可以复制此代码到cmd运行↓
`git clone https://github.com/Lkhsss/163music-autocheckin.git`
<img src="./%E6%95%99%E7%A8%8B%E5%9B%BE%E7%89%87/%E5%85%8B%E9%9A%86%E9%A1%B9%E7%9B%AE.png" alt="克隆本项目" width="80%">

#### 二、配置配置文件
在`config.ini`文件中配置自己的设置
`username`为你的网易云账号电话号码
`logintype`为登录方式（`pc`、`scanqr`可选，一个是验证码登录，一个是扫描二维码登录）

#### 三、获得`music163.pkl`文件
克隆到本地后，导航到此文件夹，使用`pip install -r requirements.txt`安装运行库
然后运行`getcookie.py`文件，如果运行不成功，多半是运行环境没有配好（重新配置python，安装运行库：DecryptLogin库），或者有多个python环境（手动copy，运行getcookie.py有提示路径）

#### 四、上传仓库
再运行一遍`main.py`，确认没有运行错误或其他提示
<img src="./教程图片/正常运行.png" alt="正常运行" width="90%">
然后上传到任意仓库

#### 五、运行
在仓库首页点击`Acions`
<img src="./教程图片/点击actions.png" alt="点击actions" width="90%">
点击“网易云自动签到”即可查看详情
<img src="./教程图片/点击查看工作流运行详情.png" alt="点击查看工作流运行详情" width="90%">




### 感谢[Ysnsn的项目提供灵感](https://github.com/Ysnsn/wangyiyun-action)
> （但是他的项目不能用了，额而且好像有很多这个项目副本，不知道谁是原作者）
### 感谢[DecryptLogin的实战案例](https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/EXAMPLES.html)
###感谢[Charles的皮卡丘](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw)提供的原脚本