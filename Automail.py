# import smtplib, ssl
# import pandas as pd

# mail_csv = pd.read_csv('Mail_csv.csv',index_col='Index')

# def automail_generator(absentee):
#     mail='vinitkavya@gmail.com'
#     stud_dict ={}
#     for names in absentee:
#         stud_dict[names]=mail
#     port = 587  # For starttls
#     smtp_server = "smtp.gmail.com"
#     sender_email = "sharmavinit.1008@gmail.com"
#     receiver_email = mail
#     password = input("Type your password and press enter:")
#     message = """\
#     Subject: Hi there
#     Im sending an email through python code."""
#     context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo() 
#         server.starttls(context=context)
#         server.ehlo() 
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message) 

# automail_generator(absentee=['Vinit'])

from twilio.rest import Client

SID = 'ACbea29700203306817038abafb4143d38'
Auth_token = '8a4e49e7e9600bf8bb82b38cbee7e60a'

cl = Client(SID,Auth_token)

cl.messages.create(body='Test message',from_='+91 98334 83697',to='+91 98334 95777')