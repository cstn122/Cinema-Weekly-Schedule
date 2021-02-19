#code from "PYTHON期末專題 電影訂票 https://www.youtube.com/watch?v=p8UeIDupR5Y&list=WL&index=2&t=0s "

from pyquery import PyQuery as pq
import smtplib
from email.mime.text import MIMEText
import time

fc1,fc2 = [],[]

while True:
    dataUrl = 'https://www.miramarcinemas.tw/Home/startordertime'
    doc = pq(url=dataUrl)
    fc1 = doc('.content .row>p').text(squash_space=False)
    print(fc1)
    
    if fc1 == fc2:
        print('No difference updated!')
        time.sleep(10)
    else:
        gmail_user = 'cstn122@gmail.com'
        gmail_pswd = 'Frontheart75592'
        
        msg = MIMEText(fc1)
        msg['Subject'] = 'New Movie List'
        msg['From'] = gmail_user
        msg['To'] = gmail_user
        
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user,gmail_pswd)
        server.send_message(msg)
        server.quit()
        
        fc2 = fc1
        print('New movielist sent!')
        time.sleep(10)