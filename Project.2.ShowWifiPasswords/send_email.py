import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_mail(receiver_email):
    sender_email = 'SENDER EMAIL ADDRESS'
    password = 'PASSWORD'
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Codewithperesthayal-Passwords"
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    html = """\
    <html>
      <body>
        <p><br>
           <i style='color:red;'>Passwords are ready!</i><br/>
           <a href="https://www.instagram.com/codewithperesthayal"><b>@Codewithperesthayal</b></a><br/>
           Have a great day :)
        </p>
      </body>
    </html>
    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # Attach File
    file='./passwords.txt'
    message.attach(part1)
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(file, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
    message.attach(attachment)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
