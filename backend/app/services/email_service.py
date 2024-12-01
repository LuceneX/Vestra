# services/email_service.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to: str, subject: str, body: str):
    """Send an email using SMTP."""
    from_email = "youremail@example.com"
    password = "yourpassword"
    server = "smtp.example.com"
    port = 587

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(server, port) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(from_email, password)
            smtp_server.sendmail(from_email, to, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
