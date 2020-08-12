import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sanjay Das'
email['to'] = 'sanjayda15@gmail.com'
email['subject'] = 'YOU CAN DO IT !!'

email.set_content('I will be a python Developer')

with smtplib.SMTP(host='smtp.gmail.com', port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sanjayda15@gmail.com', 'SwapanMithu@1958')
    smtp.send_message(email)
    print('message sent')
