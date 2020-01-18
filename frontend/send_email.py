# import smtplib, ssl, sys

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# # change your gmail account settings and enable less secure apps
# # me == my email address
# # you == recipient's email address



# # Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
# html = """\
# <html>    
#   <head></head>
#   <body>
#     <p>Hi!<br>
#        How are you? sending from function <br>
#        Here is the <a href="http://www.python.org">link</a> you wanted.
#     </p>
#   </body>
# </html>
# """

# # Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(text, 'plain')

     

# if __name__ == "__main__":
#   sendEmail("hkchheda", html)
#   # sendEmail(sys.argv[1], sys.argv[2])