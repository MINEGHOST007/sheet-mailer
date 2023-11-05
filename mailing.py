import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import random
import secrets_default as secrets

def send_mail(name,to_email,fromEmail,subject):
    email_password = secrets.EMAIL_PASSWORD
    msg = EmailMessage()

    asparagus_cid = make_msgid()
    msg.add_alternative(f"""\
        <html lang="en">
        <body>

            <center><img src="https://i.imgur.com/0YsGhjH.png" alt="header img" width="400px"></center>
            <p>
            We look forward to seeing your students showcase their skills and knowledge. If you have any questions or concerns, please do not hesitate to reach out to us.
            </p>
            <p>
            Regards,<br>
            Team <b>EDC</b>
            </p>
        </body>
        </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = to_email
    msg.add_header('status','unsent')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromEmail, email_password)
    s.send_message(msg)
    s.quit()