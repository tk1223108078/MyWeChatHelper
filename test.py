#-*-coding:utf-8-*-
import sys
import itchat

# 设置编码
reload(sys)  
sys.setdefaultencoding('utf8')   

# enableCmdQR=True为了可以命令行显示二维码
itchat.auto_login()
itchat.send('Hello, filehelper', toUserName='filehelper')