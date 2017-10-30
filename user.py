#coding:utf-8

import base64
import re

print '''
本程序只适用于在linux系统上使用python版ssr客户端
ssr的服务器版本身包含有客户端，只需要从github上下载服务器端放入本机即可使用
下载软件后将本程序放入shadowsocksr/shadowsocks目录后运行即可
也可以运行本程序后将生成的user-config.json文件复制到此目录下
因每次更换服务器都需要手动更改user-config.json很蛋疼故此写了这个程序
高手请忽略，按回车键开始
'''
hello = raw_input()

print '''
请输入SSR地址码（就是ssr://dhfjsjsjxjdjs那一串玩意儿，嫌太长？你丫不会复制粘帖吗）
手动配置服务器信息请输入1'''

ssrerror = raw_input()
error = True
while error:
    if ssrerror == "1":
        break
    try:
        ssrerrorde = re.split('[:/]',ssrerror)
        ssrurl = ssrerrorde[3]
        missing_padding = 4 - len(ssrurl) % 4
        if missing_padding:
            ssrurl += b'='* missing_padding
        ssrurl = base64.urlsafe_b64decode(ssrurl)
        ssrurl = re.split('[:/?&]',ssrurl)
        serverip = ssrurl[0]
        serverport = ssrurl[1]
        password = ssrurl[5]
        missing_padding = 4 - len(password) % 4
        if missing_padding:
            password += b'='* missing_padding
        password = base64.urlsafe_b64decode(password)
        method = ssrurl[3]
        protocol = ssrurl[2]
        obfs = ssrurl[4]
        error = False
    except:
        print "导入失败，请确认输入的SSR地址是否正确"
        ssrerror = raw_input("请输入SSR地址码，或输入1手动配置\n")
        error = True
ssrhead = ssrerror

if ssrhead == "1":
    serverip = raw_input("请输入服务器IP地址:\n")
    serverport = raw_input("请输入服务器端口:\n")
    print "请输入本机代理地址，默认127.0.0.1，使用默认请回车"
    localaddress = raw_input()
    if localaddress == "":
        localaddress = "127.0.0.1"
    print "请输入本机代理端口，默认1080，使用默认请回车"
    localport = raw_input()
    if localport == "":
        localport = "1080"
    password = raw_input("请输入密码:\n")

    print '''
none 不加密直接回车
1="table"
2="rc4"
3="rc4-md5"
4="rc4-md5-6"
5="aes-128-cfb"
6="aes-192-cfb"
7="aes-256-cfb"
8="aes-128-ctr"
9="aes-192-ctr"
10="aes-256-ctr"
11="bf-cfb"
12="camellia-128-cfb"
13="camellia-192-cfb"
14="camellia-256-cfb"
15="cast5-cfb"
16="des-cfb"
17="idea-cfb"
18="rc2-cfb"
19="seed-cfb"
20="salsa20"
21="chacha20"
22="chacha20-ietf"
    
请输入对应的加密方式数字'''
    error = True
    while error:
        method = raw_input()
        if method == "":
            method == ""
            error = False
        elif method == "1":
            method = "table"
            error = False
        elif method == "2":
            method = "rc4"
            error = False
        elif method == "3":
            method = "rc4-md5"
            error = False
        elif method == "4":
            method = "rc4-md5-6"
            error = False
        elif method == "5":
            method = "aes-128-cfb"
            error = False
        elif method == "6":
            method = "aes-192-cfb"
            error = False
        elif method == "7":
            method = "aes-256-cfb"
            error = False
        elif method == "8":
            method = "aes-128-ctr"
            error = False
        elif method == "9":
            method = "aes-192-ctr"
            error = False
        elif method == "10":
            method = "aes-256-ctr"
            error = False
        elif method == "11":
            method = "bf-cfb"
            error = False
        elif method == "12":
            method = "camellia-128-cfb"
            error = False
        elif method == "13":
            method = "camellia-192-cfb"
            error = False
        elif method == "14":
            method = "camellia-256-cfb"
            error = False
        elif method == "15":
            method = "cast5-cfb"
            error = False
        elif method == "16":
            method = "des-cfb"
            error = False
        elif method == "17":
            method = "idea-cfb"
            error = False
        elif method == "18":
            method = "rc2-cfb"
            error = False
        elif method == "19":
            method = "seed-cfb"
            error = False
        elif method == "20":
            method = "salsa20"
            error = False
        elif method == "21":
            method = "chacha20"
            error = False
        elif method == "22":
            method = "chacha20-ietf"
            error = False
        else:
            print "请输入正确的数字"
            error = True

    print '''
1="origin"
2="verify_simple"
3="verify_sha1"
4="auth_sha1"
5="auth_sha1_v2"
6="auth_sha1_v4"
7="auth_aes128_sha1"
8="auth_aes128_md5"
9="auth_chain_a"
10="auth_chain_b"
11="auth_chain_c"
12="auth_chain_d"
    
请输入对应的协议插件数字'''
    error = True
    while error:
        protocol = raw_input()
        if protocol == "1":
            protocol = "origin"
            error = False
        elif protocol == "2":
            protocol = "verify_simple"
            error = False
        elif protocol == "3":
            protocol = "verify_sha1"
            error = False
        elif protocol == "4":
            protocol = "auth_sha1"
            error = False
        elif protocol == "5":
            protocol = "auth_sha1_v2"
            error = False
        elif protocol == "6":
            protocol = "auth_sha1_v4"
            error = False
        elif protocol == "7":
            protocol = "auth_aes128_sha1"
            error = False
        elif protocol == "8":
            protocol = "auth_aes128_md5"
            error = False
        elif protocol == "9":
            protocol = "auth_chain_a"
            error = False
        elif protocol == "10":
            protocol = "auth_chain_b"
            error = False
        elif protocol == "11":
            protocol = "auth_chain_c"
            error = False
        elif protocol == "12":
            protocol = "auth_chain_d"
            error = False
        else:
            print "请输入正确的数字"
            error = True

    protocolparam = raw_input("请输入协议参数，不使用参数请回车:\n")

    print '''
1="plain"
2="http_simple"
3="http_post"
4="tls_simple"
5="tls1.2_ticket_auth"
6="tls1.2_ticket_fastauth"
    
请输入对应的混淆参数的数字'''
    error = True
    while error:
        obfs = raw_input()
        if obfs == "1":
            obfs = "plain"
            error = False
        elif obfs == "2":
            obfs = "http_simple"
            error = False
        elif obfs == "3":
            obfs = "http_post"
            error = False
        elif obfs == "4":
            obfs = "tls_simple"
            error = False
        elif obfs == "5":
            obfs = "tls1.2_ticket_auth"
            error = False
        elif obfs == "6":
            obfs = "tls1.2_ticket_fastauth"
            error = False
        else:
            print "请输入正确的数字"
            error = True

    print '''
请输入混淆参数
示例:baidu.com (不需要加http)
不使用参数请回车'''
    obfsparam = raw_input()

else:
    print "请输入本机代理地址，默认127.0.0.1，使用默认请回车"
    localaddress = raw_input()
    if localaddress == "":
        localaddress = "127.0.0.1"
    print "请输入本机代理端口，默认1080，使用默认请回车"
    localport = raw_input()
    if localport == "":
        localport = "1080"
    protocolparam = raw_input("请输入协议参数，不使用参数请回车:\n")
    print '''
请输入混淆参数
示例:baidu.com (不需要加http)
不使用参数请回车'''
    obfsparam = raw_input()

user='''{
    "server": "%s",
    "server_ipv6": "::",
    "server_port": %s,
    "local_address": "%s",
    "local_port": %s,

    "password": "%s",
    "method": "%s",
    "protocol": "%s",
    "protocol_param": "%s",
    "obfs": "%s",
    "obfs_param": "%s",
    "speed_limit_per_con": 0,
    "speed_limit_per_user": 0,

    "additional_ports" : {},
    "timeout": 120,
    "udp_timeout": 60,
    "dns_ipv6": false,
    "connect_verbose_info": 0,
    "redirect": "",
    "fast_open": false
}
'''%(serverip,serverport,localaddress,localport,password,method,protocol,protocolparam,obfs,obfsparam)
with open('user-config.json','w') as f:
	f.write(user.encode("utf-8"))
print user+"\n"+"请检查输入是否有误，若需要修改请重新执行程序。\n启动ssr请在终端切换至shadowsocksr/shadowsocks目录执行python local.py -d start"
