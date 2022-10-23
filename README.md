## 一个简单的，基于 Github Action 的网易云自动签到脚本

> 为了需要把[Charles 的皮卡丘](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw)的代码改了一下，做了个可以用 github action 的网易云签到脚本。配置好后可以一直不用管。不用自备服务器，没有其他花里胡哨功能。

> 本人学术不精，同时也暂时没有时间改良登录配置，将就一下吧

---

### Github Actions 部署指南

运行环境：windows 11
python: 3.9.5
运行库：DecryptLogin

---

#### 一、Fork此项目
![](./%E6%95%99%E7%A8%8B%E5%9B%BE%E7%89%87/fork.png)
---
#### 二、在github action中扫码登陆

#### 六、注意事项

1. 该工作流每天自动运行四次
    > 可以通过修改`autocheckin.yml`来更改时间和次数

2. 可以通过点击 ***Star*** 手动运行。

---

### 感谢[Ysnsn 的项目提供灵感](https://github.com/Ysnsn/wangyiyun-action)

> （但是他的项目不能用了，额而且好像有很多这个项目副本，不知道谁是原作者）

### 感谢[DecryptLogin 的实战案例](https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/EXAMPLES.html)

###感谢[Charles 的皮卡丘](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw)提供的原脚本
