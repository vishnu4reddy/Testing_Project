import smtplib
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'vishnuvardhanuv36@gmail.com'
recipient_email = 'vishnuvardhanuv36@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent via SMTP.'

# Create a MIMEText object with the email content
msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

# Connect to Gmail's SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, 'vishnu16REDDY@')
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
