## 一个简单的，基于 Github Action 的网易云自动签到脚本
目前项目运行状态：[![autowork](https://github.com/Lkhsss/163music-autocheckin-private-/actions/workflows/autocheckin.yml/badge.svg?branch=main&event=schedule)](https://github.com/Lkhsss/163music-autocheckin-private-/actions/workflows/autocheckin.yml)

> 为了需要把[Charles 的皮卡丘](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw)的代码改了一下，做了个可以用 github action 的网易云签到脚本。配置好后可以一直不用管。不用自备服务器，没有其他花里胡哨功能。

> 本人学术不精，同时也暂时没有时间改良登录配置，将就一下吧

---

### Github Actions 部署指南

运行环境：windows 11
python: 3.9.5
运行库：DecryptLogin

---

#### 一、克隆此项目到本地

1.可以点击**下载**按钮下载 zip 包

<img src="./%E6%95%99%E7%A8%8B%E5%9B%BE%E7%89%87/%E4%B8%8B%E8%BD%BDzip%E5%8C%85.png" alt="下载ZIP包" width="40%">

2.也可以复制此代码到 cmd 运行 ↓
`git clone https://github.com/Lkhsss/163music-autocheckin.git`

<img src="./%E6%95%99%E7%A8%8B%E5%9B%BE%E7%89%87/%E5%85%8B%E9%9A%86%E9%A1%B9%E7%9B%AE.png" alt="克隆本项目" width="80%">

---

#### 二、配置配置文件

在`config.cfg`文件中配置自己的设置

`username`为你的网易云账号电话号码

`logintype`为登录方式（`pc`、`scanqr`可选，一个是验证码登录，一个是扫描二维码登录）

---

#### 三、运行 run.bat，获得`music163.pkl`文件

点击`run.bat`，将自动运行，请扫码登陆
如果不能扫码，请在`config.cfg`中修改为验证码登陆

---

#### 四、上传仓库

将本仓库上传至你的任意仓库（最好是私有仓库，不然会泄露你的信息）

> **注意检查主目录中有没有`music163.pkl`和`music163.py`**

---

#### 五、运行

在仓库首页点击`Acions`

<img src="./教程图片/点击actions.png" alt="点击actions" width="90%">

再点击 **I understand my workflows, go ahead and enable them**

![点击确认](https://i.loli.net/2020/07/27/pyQmdMHrOIz4x2f.png)

点击“网易云自动签到”即可查看详情

<img src="./教程图片/点击查看工作流运行详情.png" alt="点击查看工作流运行详情" width="90%">

如图，左边显示绿勾时，就表示工作流工作正常

<img src="./教程图片/成功运行.png" alt="点击查看工作流运行详情" width="90%">

---

#### 六、注意事项

1. 该工作流每天自动运行四次
   > 可以通过修改`autocheckin.yml`来更改时间和次数
2. 可以通过点击 **_Star_** 手动运行。

---

#### 七、有问题欢迎 issue!

> 注：我一般周一到周五不在

---

### 感谢[Ysnsn 的项目提供灵感](https://github.com/Ysnsn/wangyiyun-action)

> （但是他的项目不能用了，额而且好像有很多这个项目副本，不知道谁是原作者）

### 感谢[DecryptLogin 的实战案例](https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/EXAMPLES.html)

###感谢[Charles 的皮卡丘](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw)提供的原脚本
