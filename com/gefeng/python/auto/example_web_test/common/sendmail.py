# coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail(object):

    def __init__(self):
        self.smtpserver = "smtp-mail.outlook.com"
        self.port = 587
        self.sender = "gefeng_zhang@outlook.com"
        self.psw = "Xiao@0715"
        self.receiver = 'gefeng_zhang@outlook.com'

    def email_send(self, report):
        with open(report, 'rb') as file:
            mail_body = file.read()

            # 创建一个带附件的邮件正文
            msg = MIMEMultipart()
            # 以测试报告作为邮件正文
            msg.attach(MIMEText(mail_body, "html", "utf-8"))
            report_file = MIMEText(mail_body, "html", "utf-8")

            # 定义附件名称
            report_file["Content-Dispositon"] = "attachment; filename = " + reportName
            msg.attach(report_file)

            msg["Subject"] = "自动化测试报告：" + reportName
            msg["From"] = self.sender
            msg["To"] = self.receiver

            try:
                server = smtplib.SMTP(self.smtpserver)
                server.login(self.sender, self.psw)
                server.sendmail(msg["From"], msg["To"].split(";"), msg.as_string())
                server.quit()
            except smtplib.SMTPException:
                print("邮件发送失败。。。。")




