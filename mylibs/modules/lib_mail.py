import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl


def send(to, subject, body, headers={}):
    from_email = getValue(headers, 'from_email', 'info@bee.raindrop.jp')
    bcc = getValue(headers, 'bcc', '')
    print(from_email, to, bcc, subject, body)
    msg = create_message(from_email, to, bcc, subject, body)
    return _send(from_email, to, msg)


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def _send(from_addr, to_addrs, msg):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.lolipop.jp', 465, timeout=5)
    smtpobj.login('info@bee.raindrop.jp', '9pIh61243A--P_8r')
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


def getValue(d, proparty, default):
    if proparty in d:
        return d[proparty]
    else:
        return default
