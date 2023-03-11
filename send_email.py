
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#put your gmail id, password, sender address over here

email_user = 'charis.rhea@outlook.com' #enter outlook mailid
email_password = 'RheaChari$'
email_send = 'charis.rhea@outlook.com' #enter outlook mailid

subject = 'enter subject'


msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
body = 'log file'
msg.attach(MIMEText(body,'plain'))
filename='file.log'
attachment =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.office365.com',587) #write the correct port no. and smtp corresponding to the email
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()

