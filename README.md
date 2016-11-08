# Sisyphus

帮助内网中的Raspberry Pi稳定保持ssh反向代理。

## Why Sisyphus

Raspberry Pi可能处于家庭（或宿舍）等环境中，没有公网IP。

为了在其他环境中连接到Raspberry Pi，需要一台具有公网IP的电脑充当Server，为Raspberry Pi充当SSH反向代理。

PC <----> Server <----> Raspberry Pi

但SSH反向代理并不稳定，Server常常会丢失Raspberry Pi的连接。

为了让Raspberry Pi和Server之间保持较为稳定的连接，这里提供了一种定时检测连接状态并及时恢复的机制。

Sisyphus运行在Raspberry Pi上，Server只需开启ssh服务即可。

## 工作方式

每15分钟检查一次SSH反向代理是否正常，若不正常则重新设置SSH反向代理。保证Raspberry Pi可访问。

## Requirement

Raspberry Pi:
- Python3

## 使用方法

首先将源代码clone到本地：

```bash
git clone https://github.com/ex44559/Sisyphus
```

**将cronfile中的目录更改为实际源代码的目录**

将cronfile复制到/etc/crontab目录中：

```bash
cp <目录>/Sisyphus/cronfile /etc/crontab
```

重新启动cron服务(适用于CentOS 7 / Debian 8)：

```bash
systemctl restart cron
```

**修改sisyphus.py,将其中的```100.100.100.100```替换为Server的IP，将其中的```haha```替换为Server的密码即可。**

## 其他

Sisyphus，即西西弗斯，一次又一次将巨石推上山顶。这个脚本也是一次又一次检查SSH连接。:)