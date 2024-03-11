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
<html>
<body>
<div style="text-align: center;">
    <img src="https://i.imgur.com/mHVAo4S.png" alt="E-Summit Logo" style="width: 60%; height: auto;">
</div>
<p><strong>Dear Participant,</strong></p>
<p>Congratulations on participating in BizCup 6.0 organized by the Entrepreneurship Development Cell at NIT Durgapur!</p>
<p>We appreciate your enthusiasm and dedication to exploring entrepreneurial skills through this event.</p>
<p>Attached is your participation certificate for BizCup 6.0:</p>
<p><a href="certificate_link_here" style="text-decoration: none;"><strong>Participation Certificate</strong></a></p>
<p>Thank you for being a part of our entrepreneurial community. We hope to see you in future events!</p>
<p>Best Regards,<br>
<strong>Entrepreneurship Development Cell,</strong><br>
NIT Durgapur,<br>
Contact: 8335810111, 9007123507</p>
</body>
</html>
""", subtype='html')

    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = to_email
    msg.add_header('status','unsent')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromEmail, email_password)
    s.send_message(msg)
    s.quit()

# <html>
# <body>
# <div style="text-align: center;">
#     <img src="https://i.imgur.com/mHVAo4S.png" alt="E-Summit Logo" style="width: 60%; height: auto;">
# </div>
# <p><strong>Dear School,</strong></p>
# <p>On behalf of the Entrepreneurship Development Cell, NIT Durgapur, I am excited to extend an invitation to your esteemed institution.</p>
# <p>We cordially invite you to participate in our upcoming online event, <strong>Quiz-a-Preneur</strong>, part of our annual entrepreneurial fest, <strong>E-Summit</strong>. E-Summit serves as a vibrant platform for budding entrepreneurs, students, and professionals to exchange ideas, learn from industry leaders, and showcase creative minds. <strong>Quiz-a-Preneur</strong> is tailored to evaluate participants' business acumen and entrepreneurial knowledge through engaging quiz rounds, promising to be an intellectually stimulating and enjoyable experience.</p>
# <p><strong>Event Details:</strong></p>
# <ul>
# <li><strong>Event Name:</strong> Quiz-a-Preneur</li>
# <li><strong>Date & Time:</strong> 5:30pm to 7:30pm on 23rd March (Round 1); 11:30am to 1:30pm on 24th March (Round 2)</li>
# <li><strong>Eligibility:</strong> Students from Class 8th to 12th</li>
# <li><strong>Platform:</strong> Website/Google Meet</li>
# <li><strong>Registration Link:</strong> <a href="https://quiz.edcnitd.co.in">https://quiz.edcnitd.co.in</a></li>
# <li><strong>Prizes:</strong> Certificates and prizes worth Rs 3k.</li>
# </ul>
# <p>Participation in <strong>Quiz-a-Preneur</strong> offers your students not only enrichment but also the opportunity to network with like-minded individuals and showcase their talent in Eastern India's second-largest entrepreneurial fest, <strong>E-Summit</strong>. If there are any inquiries or if you require further information, please do not hesitate to reach out to us.</p>
# <p>We eagerly anticipate your enthusiastic participation in <strong>Quiz-a-Preneur</strong> and look forward to witnessing your students' entrepreneurial prowess at <strong>E-Summit, NIT Durgapur</strong>.</p>
# <p>Thank you for considering our invitation, and we eagerly await your response.</p>
                        
# <p>Attached is the poster for the event.<br>
# <a href="https://drive.google.com/file/d/1QifTtzbHrDnuC9v3aEyf9VJI-WI0J1lh/view?usp=sharing" style="text-decoration: none;"><strong>Poster</strong></a><br></p>
# Best Regards,<br>
# <strong>Entrepreneurship Development Cell,</strong><br>
# NIT Durgapur,<br>
# Contact: 8335810111, 9007123507</p>
# </body>
# </html>