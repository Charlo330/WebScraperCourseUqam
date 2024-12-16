import os

from dotenv import load_dotenv

load_dotenv()

email_sender = os.getenv("SENDER_EMAIL")
email_receiver = os.getenv("RECEIVER_EMAIL")
email_pass = os.getenv("EMAIL_PASSWORD")
smtp_port = int(os.getenv("SMTP_PORT"))
smtp_server = os.getenv("SMTP_SERVER")

subject = os.getenv("EMAIL_SUBJECT")
course_acronym = os.getenv("COURSE_ACRONYM")
course_name = os.getenv("COURSE_NAME")
class_url = os.getenv("COURSE_URL")

time_sleep = int(os.getenv("TIME_INTERVAL"))
