#!/usr/bin/python3

import base64
import smtplib, ssl
from getpass import getpass
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.mime, email.mime.nonmultipart, email.charset

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

# password = getpass("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

sender_email="sham72942@gmail.com"
receiver_email="sham72942@gmail.com"

text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
<body>

<h1>The th element</h1>

<p>The th element defines a header cell in a table:</p>

<table>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$80</td>
  </tr>
</table>

</body>
</html>"""

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Turn these into plain/html MIMEText objects
cs=email.charset.Charset('UTF-8')
cs.body_encoding = email.charset.BASE64

part1=email.mime.nonmultipart.MIMENonMultipart('text', 'plain')
part1.set_payload(text, charset=cs)
part2=email.mime.nonmultipart.MIMENonMultipart('text', 'html')
part2.set_payload(html, charset=cs)

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

print(message)

# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# 	server.login(sender_email, password)
# 	server.sendmail(sender_email, receiver_email, message.as_string())
# 	server.quit()

# print("mail_sent")
