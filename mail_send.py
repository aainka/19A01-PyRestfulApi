# -*- coding:utf-8 -*-
 
import smtplib
import os
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class cEMail():
    # Daily Limitation : 500 send / day
    # eMail Provide    SMTP ServerName    Port    
    # Live             smtp.live.com      587 
    # GMail            smtp.gmail.com     587    
    def __init__(self,smtpServer, password='password'):
        #print( "cEMail __init__")
        self.smtpServer=smtpServer
        self.smtp = smtplib.SMTP('smtp.gmail.com')
        self.smtp.ehlo()      # say Hello
        self.smtp.starttls()  # TLS  
        self.smtp.login(self.smtpServer, password)
    
    def __del__(self):
        #print( "cEMail __del__")
        try:self.smtp.quit()
        except:pass
    
    def send(self,toEMail,subject,message):
        print("mail.send subject "+subject)
        #msg = MIMEText(message)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['Date'] = formatdate(localtime=True)
        msg['From'] = self.smtpServer
        msg['To'] = toEMail
        part1 = MIMEText(message,'html')
        msg.attach(part1)
        #msg.add_header('Content-Type',"text/html")
        #msg.set_payload(message)
        fromEMail=self.smtpServer
        self.smtp.sendmail(fromEMail, toEMail, msg.as_string())
        
if __name__ == '__main__':

    smtp_server='aainka@gmail.com'
    smtp_server_password='inka4723'
    m_eMail =cEMail(smtp_server,smtp_server_password)
    
    toMail='jaeyoung.jeon@ericsson.com'
    Subject='Test Mail'
    Message='TTT test'
    m_eMail.send(toMail,Subject,Message)


