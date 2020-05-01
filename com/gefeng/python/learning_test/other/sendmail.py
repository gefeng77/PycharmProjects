# coding=utf-8
import smtplib
from email.mime.text import MIMEText


# 1.--------跟发件相关的参数---------
smtpserver = "smtp-mail.outlook.com"        # 发件服务器
port = 587                                  # 端口
sender = "gefeng_zhang@outlook.com"         # 账号
psw = "Xiao@0715"                           # 密码
receiver = "zhangdm@outlook.com"            # 接收人

# 2.--------编辑邮件的内容---------
subject = "just for testing"
body = '<p>这是一封测试邮件，请忽略。</p>'       # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg["from"] = sender
msg["to"] = receiver
msg["subject"] = subject

# 3.--------发送邮件---------
smtp = smtplib.SMTP()
smtp.connect(smtpserver)                             # 连接服务器
smtp.ehlo()                                          # 登录前必须加上L23，L24，否则报错
smtp.starttls()
smtp.login(sender, psw)                              # 登录
smtp.sendmail(sender, receiver, msg.as_string())     # 发送
smtp.quit()                                          # 关闭
