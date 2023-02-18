# a = 10
# #条件满足的时候会执行循环while代码
# while a > 1:
#     print(a)
#     break
#     a = a - 1  #自减
# #break 终止循环
# #条件满足会一直执行下去，加如break会终止程序
# for i in range(10): [0,1,2,3,4,5,6,7,8,9]
#     if i % 2 ==0:
#     continue
#         print(i)



#oython代码结构


#包/库
#1.标准库-python自带的工具寒素
# os   操作系统
# sys   环境变量
# time   时间相关
#  dateime  时间相关
#  random   随机数


#包   
import os
print(os.getcwd())#获取当前文件所在的路径
print(os.cpu_count()) #获取cpu的核心
#  os.mkdir('./dayuer')#创建文件夹
#创建文件使用的open函数来创建
#  open('./')
import sys
print(sys.path) #获取当前的运行环境

import time
print(time.localtime().tm_year)   #获取
print(time.localtime().tm_mon)
print(time.localtime().tm_mday)


#time.sleep(10)   #代码执行等待10S  web自动化中广泛使用


import random

a = random.randint(10000,99999)
print(a)
  

#导入 第三方库/包   #大佬们开发上传到python的应用商店的
#   request   HTTP 请求
#   pymysql   python  操作数据的库的
#   selenium     WEB自动化的包
#
#
#
#在cmd里面输入pip3 list   查看已经安装的第三方包
#pip3 install  requests -i https://pypi.tuna.tsinghua.edu.cn/simple    
#pip3 install  pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple      
#pip3 install  pytest -i https://pypi.tuna.tsinghua.edu.cn/simple      
#因为是在大洋彼岸所以使用清华园源码安装  #   
#pip3 uninstall 包名  卸载包
#证书错误的情况下，去下载强制信任证书：  

#自定包/自定义包    
#    分层执行
#   封装     #1.把相同功能的代码使用函数/类进行二次封装。提高代码的使用率
#   自定义包  # 创建文件夹  
              # 