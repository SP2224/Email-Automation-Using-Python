import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='senders email id'
to_addr=['jgduyfh@gmail.com','hisbdcuegf.@gmail.com']  #these are the fake mails which doesn't even exist
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='just to check'

body='Type anything here'

msg.attach(MIMEText(body,'plain'))

email='---enter your email here---'
password='----enter your password here----'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()