# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time

# 1.--------跟发邮件相关的参数---------
smtpserver = "smtp-mail.outlook.com"        # 发件服务器
port = 587                                  # 端口
sender = "gefeng_zhang@outlook.com"         # 账号
psw = "Xiao@0715"                           # 密码
receiver = "gefeng_zhang@outlook.com"       # 接收人

# 2.--------编辑邮件的内容---------
# 读文件
file_name = "english 2.docx"
with open(file_name, "rb") as fp:
    mail_body = fp.read()

subject = "just for testing"

# 创建一个带附件的实例
msg = MIMEMultipart()

# 加邮件头
msg["from"] = sender
msg["to"] = receiver
# 主题指定utf-8编码，否则中文会有乱码
msg["subject"] = Header('subject', 'utf-8')
sendtime = time.strftime("%h:%m:%s", time.localtime(time.time()))

# 邮件正文
# 注意，要指定邮件内容的编码为utf-8，否则中文会有乱码
body = MIMEText("测试邮件，请忽略。。。。", "plain", "utf-8")
msg.attach(body)

# 添加附件
att = MIMEText(open(file_name, 'rb').read(), 'base64', 'gb2312')
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename = %s' % file_name.encode('gb2312')
msg.attach(att)

# 3.--------发送邮件---------
smtp = smtplib.SMTP()
smtp.connect(smtpserver)                             # 连接服务器
smtp.ehlo()                                          # 登录前必须加上L23，L24，否则报错
smtp.starttls()
smtp.login(sender, psw)                              # 登录
try:
    smtp.sendmail(sender, receiver, msg.as_string())     # 发送
    print("发送成功！")
except smtplib.SMTPException:
    print("Error: 无法发送邮件！")

smtp.quit()           # 关闭
