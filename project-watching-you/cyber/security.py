
import smtplib
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rambudavincent0@gmail.com','Rambuda360')
    server.sendmail('rambudavincent0@gmail.com', 'onrambu022@student.wethinkcode.co.za','Theres is movement at your residence!!!')