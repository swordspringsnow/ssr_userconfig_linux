user-config.json editor
===========

2017/11/02
第三次更新，使用类和list精简了100行重复代码。

2017/10/30
第二次更新，加入SSR地址码合法性判断功能，完善选项输入错误的处理。

2017/10/28
第一次更新，加入导入SSR链接功能，直接复制粘帖链接字符串到程序，程序可以自动转化成服务器配置。

纯粹是学习python的练手产品，勿喷。仅适用于在LINUX上使用SSR PYTHON版客户端时生成USER-CONFIG.JSON配置文件。在linux上用python版ssr上网有两个不方便的地方，每次更换服务器地址都是重新编辑USER-CONFIG文件，不能自动导入网上常见的SSR地址码，故此有个这个程序。

下载user.py后将其放入shadowsocksr/shadowsocks目录后运行即可
也可以运行user.py后将生成的user-config.json文件复制到此目录下
