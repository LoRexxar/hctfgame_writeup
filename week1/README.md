# hctf_game_week1_writeup

标签（空格分隔）： blog ctf 

---
假期难得有时间空闲下来，就和协会的小伙伴组织了一次比较简单的ctf比赛针对学校的学弟学妹们，这里就贴上每一次的writeup，以供整理复习用。

<!--more-->

## WEB

###  WEB从0开始之PHP代码审计0     POINT: 100 DONE

题目ID： 55
题目描述： http://ctf.lazysheep.cc:8081/web1.php
Hint: 前置技能：PHP

题目的原题是出在hctf2015的fuck===，出题思路来自[http://www.secbox.cn/hacker/1889.html](http://www.secbox.cn/hacker/1889.html).
payload: ?a[]=adsa&b[]=dsadsa
这里之所以===能过，是因为在php中，md5不能加密数组，会返回null，null==null返回flag

## MISC

###  MISC 驾驶技术科目一     POINT: 100 DONE

题目ID： 36
题目描述： 如果玩转 MISC 快来开始你的科目一吧！ 链接: http://pan.baidu.com/s/1c1c7fiC 密码: cyyd
Hint: 噫 都上些啥站呀

科目一比较简单，和之前的流量分析类似，大概就是一个http明文请求，仔细找找很快就能找到。flag中顺便找到科目二的入口。

### MISC 驾驶技术科目二     POINT: 100 DONE

题目ID： 37
题目描述： 考完科目一的小伙伴快过来科目二啦，早上上路，争当中国好司机。
Hint: 无

科目二找到后发现是一张图片，这里使用到一个linux下的工具，binwalk，可以发现图片是由多个文件合并的，使用foremost就可以把所有的东西拆开来，得到flag的二维码，扫码getflag。

###  MISC从0开始之编码1     POINT: 75 DONE

题目ID： 49
题目描述： 老司机的题目做不出来？丢一题简单的给你们做。。
http://ctf.lazysheep.cc:8081/misc1.html
Hint: base全家桶，老司机们别抢新生的前三血啊～

这里就是base全家桶了，目前好像没见过用python以外的方式做的，不过如果自己写代码实现应该也是可以的。
```
import base64
bb64=base64.b64encode('xxxxx')
bb32=base64.b32encode(bb64)
b=base64.b16endcode(bb32)
print b
```
大概就是这样...

###  MISC从0开始之流量分析1     POINT: 75 DONE

题目ID： 53
题目描述： http://ctf.lazysheep.cc:8081/misc1.pcap
Hint: 暂无HINT

比较接近一般题目的流量分析了，可以看到在最后一个http请求中请求了一个flag的zip文件。那么就需要wireshark加一个16进制编辑器把这个文件扣出来了，一般网上还是能搜到教程的，懒得赘述了。

###  CTF coding step1     POINT: 50 DONE

题目ID： 47
题目描述： 打CTF就是拿工具？ 不不不，也要写很多代码的。这个系列就是让你熟悉CTF风格的编程题目，具体的要求见题目吧のの 就是让你们多看点英文：
nc 115.29.77.78 9979
Hint: repr

nc连上发现是计算数学式子，那么开始写代码吧。
```
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('115.29.77.78',9979))
import time
sock11=sock.recv(1024)
print sock11
sock11=sock.recv(1024)
print sock11
pos2=sock11.find('=',950)
sendr = eval(sock11[945:pos2])
print sendr
sock.send(repr(sendr)+'\n')
while 1:
	sock11=sock.recv(1024)
	print sock11
	pos=sock11.find('=')
	i=sock11.find(']')
	if(i!=-1):
		sendr=eval(sock11[i+2:pos].replace('\xc3\x97','*'))
		print sendr
		sock.send(repr(sendr)+'\n')
	else:
		sendr=eval(sock11[:pos])
		print sendr
		sock.send(repr(sendr)+'\n')
sock.close()
```
 因为是第一次写socket，所以还是踩了不少坑，首先这个文件不能叫做socket.py否则不能通过编译，其次就是每一个send必须在后面加上'\n'否则不会有下一步，自己试试吧。。。
 
## crypto
 
### 密码学从0开始之1     POINT: 20 DONE

题目ID： 50
题目描述： http://ctf.lazysheep.cc:8081/cry1.html
flag不是标准格式，提交你解出的明文就行，flag全是大写
Hint: 这个简单，应该不需要hint

打开看到一堆点啊横啊就知道是摩斯密码，随便一搜都能搜到各种解码

## pentest

###  lightless&aklis的渗透教室-2     POINT: 75 DONE

题目ID： 45
题目描述： http://120.27.53.238/pentest/02/http-header.php
Hint: Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13A344 Safari/601.1
xff: 127.0.0.1

坑已经被踩完了还所做不出那就没办法了，记得要改ios99啊，hint中的是ios9的...

记得看文档啊！！！


