import smtplib
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Test mail'
msg['From'] = 'max@mustermail.com'
msg['To'] = 'til@mustermail.com'
msg.set_content('This is a test email')

with open('pic.JPG', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP('smtp.mail.net', 587) as smtp:
    smtp.starttls()
    smtp.login('max@mustermail.com', 'password')
    
    smtp.send_message(msg)