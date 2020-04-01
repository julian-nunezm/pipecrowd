import smtplib
from email.mime.text import MIMEText

def send_confirmation_email(receiver_email, receiver_name, receiver_token):
    # Set configuration email
    PORT = 587
    SMTP_SERVER = 'smtp.sendgrid.net'
    LOGIN = 'apikey'
    PASSWORD = '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'
    CONFIRMATION_LINK = 'pipecrowd-261900.appspot.com/wishlist/activate/' + receiver_token

    # Set the email message
    message = f'''<h2>Thank you {receiver_name} for registering your interest in Pipecrowd</h2>
                  <h3>We will keep you updated.</h3>
                  <a href="{CONFIRMATION_LINK}" style="text-decoration:none; display:inline-block; padding: 10px; -webkit-border-radius:50px; -moz-border-radius:50px; border-radius:50px; cursor:pointer; color:white; background-color: #1b024f; border:2px solid #1b024f;">Confirm your email!</a>'''
    SENDER_EMAIL = 'admin@pipecrowd.com'
    html_message = MIMEText(message, 'html')
    html_message['Subject'] = 'Confirmation Email from Pipecrowd'
    html_message['From'] = SENDER_EMAIL
    html_message['To'] = receiver_email

    # Send confirmation email
    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.login(LOGIN, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, html_message.as_string())