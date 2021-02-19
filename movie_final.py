#爬取電影網站資訊後作為內文，傳送email給自己

from pyquery import PyQuery as pq   #爬蟲用，需安裝 
import smtplib   #寄email用
from email.mime.text import MIMEText   #處理email內文文字
import time   #時間模組，為了每五秒爬一次

info1,info2 = [],[]   #第n次爬取的資料、第n+1次爬取的資料

while True:
    dataUrl = 'http://www.spot-hs.org.tw/schedule/schedule.html'   #要爬的網址
    doc = pq(url=dataUrl)
    info1 = doc('.member_2').text()   #網頁原始碼中要爬得資訊的所在位置
    info1 = info1.encode('ISO-8859-1')   #解碼byte
    info1 = info1.decode('utf8')   #轉換成UTF-8，讓中文字可正常檢視
    print(info1)

    if info1 == info2:   #前後爬取資訊相同，不寄email
        print('No difference updated!')
        time.sleep(5)   #休息5秒
    else:   #前後爬取資訊有更新，寄email
        gmail_user = ''   #在編譯器登入信箱帳號，寄email給自己
        gmail_pswd = ''
        
        msg = MIMEText(info1)   #內文
        msg['Subject'] = 'New Movie List'   #主旨
        msg['From'] = gmail_user   #寄件者
        msg['To'] = gmail_user   #收件者
        
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)   #登入作業
        server.ehlo()
        server.login(gmail_user,gmail_pswd)
        server.send_message(msg)
        server.quit()
        
        info2 = info1   #將後爬取的資料覆蓋成(下次)先爬取的資料
        print('New movielist sent!')
        time.sleep(5)   #休息5秒
