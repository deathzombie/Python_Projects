from email.message import EmailMessage
import ssl
import smtplib
email_send = 'priyanshsaxena787@gmail.com'
email_pass = 'yvofwkmrbzifxbvj'

email_rec = 'psaxena_be22@thapar.edu'

sub = 'Polis aa gayi polis'
body = """
Samaan ssuman ji kat liya karu
"""
em = EmailMessage()
em['From'] = email_send
em['To'] = email_rec
em['Subject'] = sub
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
    smtp.login(email_send, email_pass)
    smtp.sendmail(email_send, email_rec, em.as_string())   
