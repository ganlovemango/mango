# 发送邮件
import smtplib
from email.header import Header
from email.mime.text import MIMEText

class Emailer:
    def __init__(self,user,password,host):
        """

        :param user: 用户名
        :param password: 授权码  a123456
        :param host: 邮件服务器地址  smtp.163.com
        """
        self.user = user
        self.password = password
        self.host = host
    def send(self,sender,revicer,content,title):
        """

        :param sender: 发送者邮箱
        :param revicer:接收者邮箱
        :param content:邮件内容
        :param title:邮件标题
        :return:
        """
        # 1. 发送准备
        #参数：邮件内容，内容格式，编码格式
        message = MIMEText(content,'plain','utf-8')  #生产一个消息对象
        message['From'] = sender # 发送者
        message['To'] = revicer  #接收者
        message['Subject'] = title  #标题

        #2. 发送
        try:
            # 创建发送对象
            smtpobj = smtplib.SMTP(self.host,25)  #邮件服务器的地址和端口

            # 登录验证
            smtpobj.login(self.user,self.password)  #用户名和授权码

            #发送邮件
            smtpobj.sendmail(sender,revicer,message.as_string())
            print("发送成功")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    email = Emailer("kzx0215@163.com",'a123456','smtp.163.com')

    # 发送者必须是授权用户
    email.send("kzx0215@163.com","kzx0215@163.com","测试邮件，不需要回复",'test')

