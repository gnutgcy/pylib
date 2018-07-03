# coding: utf-8


from email.mime.text import MIMEText
import smtplib


def send_email(Subject, From, To, Cc, Text, url, username, password):
    msg = MIMEText(Text)
    msg["Subject"] = Subject
    msg["From"] = From
    msg["To"] = To
    msg["Cc"] = Cc
    smtp = smtplib.SMTP(url)
    smtp.login(username, password)
    from_addr = msg["From"]
    to_addrs = msg["To"] + msg["Cc"]
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.quit()
    pass


if __name__ == "__main__":
    pass
