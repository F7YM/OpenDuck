# OpenDuck *- 神秘鸭替代品 / Siri控制电脑*
## 介绍
### 作用
**在内网其他设备访问主机OpenDuck端口，即可在主机触发预设命令。** 使用场景：暂时离开座位，使用OpenDuck远程锁定电脑；使用Siri + 快捷指令实现Siri控制电脑......
### 技术
OpenDuck灵感来源自[神秘鸭](https://wequ.net/cn/)，使用Python开发，Nuitka打包，NSIS作为安装程序。OpenDuckManager使用easygui库。部分代码使用AI。
## 配置文件
OpenDuck配置文件位于C:\Users\你的用户名\openduck_config.json。
|  键名  |  作用  |
|  --  |  --  |
|  port  |  要使用的端口，默认1145  |
|  command  |  要执行的cmd命令，默认锁定电脑  |
|  prompt  |  返回结果，默认“搞定了。”  |
## 内网使用
### 通用思路
在内网访问`主机ip:OpenDuck端口号`。
### Siri + 快捷指令
新建快捷指令，找到“获取URL内容”操作，输入`http://主机ip:OpenDuck端口号`；添加“显示提醒”操作，关闭显示取消按钮，在输入框内选择变量为URL的内容（此操作非必需，但是Siri将不会播报返回值）。最后将快捷指令名称改为你要对Siri下的指令即可（如：锁定我的电脑）。
你也可以套用[Demo](https://www.icloud.com/shortcuts/dc769b9d29e24fc7b37b657ad73e7bcf)。
## 公网使用
**在公网使用OpenDuck有风险，出现任何安全问题与OpenDuck无关。**

使用Frp工具（如[OpenFrp](https://www.openfrp.net)）映射OpenDuck端口，访问Frp工具提供的URL即可。
