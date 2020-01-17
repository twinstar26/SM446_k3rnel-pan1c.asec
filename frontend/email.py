import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# change your gmail account settings and enable less secure apps
# me == my email address
# you == recipient's email address
me = "dhwaniagarwal.97@gmail.com"
you = "daagarwal_b17@it.vjti.ac.in"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>    
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s = smtplib.SMTP('smtp.gmail.com', 587)

s.ehlo()

s.starttls()
print("before login")
s.login('username', 'password')
print("after")
s.sendmail(me, you, msg.as_string())
s.quit()     