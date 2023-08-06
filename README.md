# MCEasySync
A tool that can sync your save with different computers<br>
本工具可用于在不同家用电脑间快速同步存档与服务端插件文件

## 使用场景

你是否因想和朋友游玩租用了一台云服务器，却因为配置低下而无法流畅游玩高版本服务器<br>
现在EasySync可快速满足你的需要<br>
你可以在服务端部署如n2n，frp等服务，搭配本软件，实现在多电脑中同步游戏文件<br>

## 功能特性

可以直接启动配置好的服务端<br>
基于md5差异确定需要更改的文件<br>
文件锁功能（手动，不太稳定）<br>
用户登录系统<br>
服务端日志存储，可以看见用户对服务器文件的操作

## 详细原理
服务端会检测server/文件夹下面的world，world_nether，world_end,mods,plugins五个文件夹，然后将他们分别存储在 (文件夹名)_formatted 文件夹内，通过将路径中的斜杠转换为"~"，将文件路径保存在文件名中，
从服务器下载有关文件的md5并与本地文件进行比对，对差异进行上传/下载操作。

## 部署

1，服务端：将Serverfile文件夹下的file_server.py上传至服务器，向第25行的字典添加用户，默认端口5000
2，客户端，直接启动main.py即可

## 结语
这是作者自学python后做的第一个开源项目
可能有一些bug和奇怪的逻辑/变量名设计
如果有时间的话，给我点一个小小的Star吧





