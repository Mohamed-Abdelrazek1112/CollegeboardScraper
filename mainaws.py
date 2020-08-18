import requests
from bs4 import BeautifulSoup
#import smtplib, ssl
import time



import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace sender@example.com with your "From" address.
# This address must be verified.
SENDER = 'abdelrazekm543@gmail.com'
SENDERNAME = 'Mo1112'

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT  = 'abdelrazekm543@gmail.com'

# Replace smtp_username with your Amazon SES SMTP user name.
USERNAME_SMTP = "AKIA5ARD2ZTRWTSX3BNK"

# Replace smtp_password with your Amazon SES SMTP password.
PASSWORD_SMTP = "BMBf+eHziAarlCOXjKQHVAu80BZS8Inur0c/vQ1ARsqT"

# (Optional) the name of a configuration set to use for this message.
# If you comment out this line, you also need to remove or comment out
# the "X-SES-CONFIGURATION-SET:" header below.
#CONFIGURATION_SET = "ConfigSet"

# If you're using Amazon SES in an AWS Region other than US West (Oregon),
# replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
# endpoint in the appropriate region.
HOST = "email-smtp.us-west-2.amazonaws.com"
PORT = 587

#port = 465  # For SSL
#password = '25712571'
closed = ["Al Rowad Intl Sch (female Only)","Al Faris Intl Sch (male Only)"]

# Create a secure SSL context
#context = ssl.create_default_context()
while True:

    URL = 'https://collegereadiness.collegeboard.org/sat/register/test-center-closings?excmpid=FB-ED-CB-1'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_="test-center-closings-group")
    for result in results:
        if None != result.find('h3', class_="state-name", string="Saudi Arabia"):
            schools = result.find_all('h3', class_="test-center-closings-content")
            for school in schools:
                print(school.text)
                if school.text in closed:
                    None
                else:
                    closed.append(school.text)
                    # The subject line of the email.
                    SUBJECT = school.text+' has been closed'

                    # The email body for recipients with non-HTML email clients.
                    #BODY_TEXT = ("Amazon SES Test\r\n"
                    #             "This email was sent through the Amazon SES SMTP "
                    #             "Interface using the Python smtplib package."
                    #            )

                    # The HTML body of the email.
                    #BODY_HTML = """<html>
                    #<head></head>
                    #<body>
                     # <h1>Amazon SES SMTP Email Test</h1>
                      #<p>This email was sent with Amazon SES using the
                        #<a href='https://www.python.org/'>Python</a>
                        #<a href='https://docs.python.org/3/library/smtplib.html'>
                        #smtplib</a> library.</p>
                    #</body>
                    #</html>
                    #            """

                    # Create message container - the correct MIME type is multipart/alternative.
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = SUBJECT
                    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
                    msg['To'] = RECIPIENT
                    # Comment or delete the next line if you are not using a configuration set
                    #msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

                    # Record the MIME types of both parts - text/plain and text/html.
                    #part1 = MIMEText(BODY_TEXT, 'plain')
                    #part2 = MIMEText(BODY_HTML, 'html')

                    # Attach parts into message container.
                    # According to RFC 2046, the last part of a multipart message, in this case
                    # the HTML message, is best and preferred.
                    #msg.attach(part1)
                    #msg.attach(part2)

                    # Try to send the message.
                    try:
                        server = smtplib.SMTP(HOST, PORT)
                        server.ehlo()
                        server.starttls()
                        #stmplib docs recommend calling ehlo() before & after starttls()
                        server.ehlo()
                        server.login(USERNAME_SMTP, PASSWORD_SMTP)
                        server.sendmail(SENDER, RECIPIENT, msg.as_string())
                        server.close()
                    # Display an error message if something goes wrong.
                    except Exception as e:
                        print ("Error: ", e)
                    else:
                        print ("Email sent!")
    time.sleep(60 * 5)
