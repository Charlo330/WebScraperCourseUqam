import smtplib
import EnvVarReader

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_sender = EnvVarReader.email_sender
email_receiver = EnvVarReader.email_receiver
email_pass = EnvVarReader.email_pass
smtp_port = EnvVarReader.smtp_port
smtp_server = EnvVarReader.smtp_server

subject = EnvVarReader.subject
course_acronym = EnvVarReader.course_acronym
course_name = EnvVarReader.course_name

em=MIMEMultipart()
em['Subject'] = "UQAM - " + course_acronym + " - Class available"
em['From'] = email_sender
em['To'] = email_receiver

def send(message):
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        message = "We found class/es available for this course : \n" + course_name + "\n\n" + message

        smtp.starttls()
        smtp.login(email_sender, email_pass)
        em.attach(MIMEText(message, 'plain'))
        smtp.sendmail(email_sender, email_receiver, em.as_string())