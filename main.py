import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import time

port = 465  # For SSL
password = '25712571'
closed = ["Al Rowad Intl Sch (female Only)","Al Faris Intl Sch (male Only)"]

# Create a secure SSL context
context = ssl.create_default_context()
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
                    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                        server.login("mowaleed1112@gmail.com", password)
                        # TODO: Send email here
                        sender_email = "mowaleed1112@gmail.com"
                        receiver_email = "mowaleed1112@gmail.com"
                        message = school.text + " was just closed in your area\n message from mohamed"
                        # Send email here
                        server.sendmail(sender_email, receiver_email, message)
    time.sleep(60 * 5)




