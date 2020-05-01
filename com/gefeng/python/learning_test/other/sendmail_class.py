# coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSender(object):
    # 类变量--在任何方法之外定义的参数
    _from = None
    _attachments = []

    def __init__(self, smtpSrv, port):
        self.smtp = smtplib.SMTP()
        print("Connecting...")
        self.smtp.connect(smtpSrv, port)
        print("Connected!")

    def login(self, user, pwd):
        self._from = user
        print("Login...")
        self.smtp.ehlo()  # 登录前必须加上L20, L21，否则报错
        self.smtp.starttls()
        self.smtp.login(user, pwd)

    def attachment(self, filename):
        '''
            添加附件
        '''
        att = MIMEText(open(filename, 'rb').read(), 'base64', 'gb2312')
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename = %s' % filename.encode('gb2312')
        self._attachments.append(att)

    def send(self, subject, content, to_addr):
        '''
            发邮件
        '''
        msg = MIMEMultipart()
        contents = MIMEText(content, "html", _charset="utf-8")
        msg["from"] = self._from
        msg["to"] = to_addr
        msg["subject"] = subject
        for att in self._attachments:
            msg.attach(att)
        msg.attach(contents)
        try:
            self.smtp.sendmail(self._from, to_addr, msg.as_string())
            print("发送成功！")
            return True
        except Exception as e:
            print(str(e) + ", 发送失败！")
            return False

    def close(self):
        self.smtp.quit()
        print("logout.")


mailSender = MailSender("smtp-mail.outlook.com", 587)
mailSender.login("gefeng_zhang@outlook.com", "Xiao@0715")
mailSender.attachment("english 2.docx")
mailSender.send("测试邮件", "这是一封测试邮件，请忽略。。。", "gefeng_zhang@outlook.com")









