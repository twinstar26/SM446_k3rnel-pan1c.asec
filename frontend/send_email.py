import smtplib, ssl, sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# change your gmail account settings and enable less secure apps
# me == my email address
# you == recipient's email address
me = "kernelpanic.asec@gmail.com"


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Response from chatbot"
msg['From'] = me


# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>    
  <head></head>
  <body>
    <p>Hi!<br>
       How are you? sending from function <br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')

def sendEmail(you, html):
  msg['To'] = you
  part2 = MIMEText(html, 'html')
  # Attach parts into message container.
  msg.attach(part2)

  # sendmail function takes 3 arguments: sender's address, recipient's address
  # and message to send - here it is sent as one string.
  s = smtplib.SMTP('smtp.gmail.com', 587)

  s.ehlo()
  s.starttls()
  print("before login")
  s.login('kernelpanic.asec@gmail.com', 'k3rnel-pan1c.asec')
  print("after")
  s.sendmail(me, you, msg.as_string())
  s.quit()     

if __name__ == "__main__":
  sendEmail(sys.argv[1] , html)
  # sendEmail(sys.argv[1], sys.argv[2])