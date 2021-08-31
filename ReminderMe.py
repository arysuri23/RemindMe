#Program to send an email
#import packages

import smtplib, ssl, datetime


from datetime import date

#dictionary of days of week
weekdays = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}
#create dictionary with string key(assignment name) and datetime value(assignment due date)

#commented out block is for user input, try to figure out how to implement this part later, for now have users just write their assignments into dictionary
'''

assignments1 = {}
a = "Y"
while(a == "Y"):
    name = input("What is the name of your assignment?")
    year = input("What year is this assignment due?")
    month = input("What month is this assignment due?")
    day = input("What day is this assignment due?")
    assignments1[name] = date(int(year), int(month), int(day))
    a = input("Would you like to enter another assignment? Enter Y or N?")

print(assignments1)
'''

assignments = {
    'Psych Chapter One' : date(2021, 8, 29),
    'CS 3330 Quiz' : date(2021, 9, 1),
    'Stat 3080 project' : date(2021, 9, 3),
    'Technosonics compo': date(2021, 9, 18),
    'Stat 2120 HW' : date(2021, 10, 10)

    #follow format to continue to add more

}

msg = "" 


countToday = 0
countWeek = 0
today = date.today()

for key in assignments:
    if(((assignments[key] - today).days < 7) and ((assignments[key] - today).days >= 0)):
        msg += "You have " + key + "  due this week on " + weekdays[assignments[key].weekday()] + "\n"
        countWeek+=1
    if assignments[key] == today:
        msg += key + "is due today! Get to work\n"
        countToday+=1



        

msg += "You have " + str(countToday) + " assignments due today and " + str(countWeek) + " due this week! Get to work!\n" 
if(countToday == 0):
    msg += "Yay! You have nothing due today!"

print(today.weekday())
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aryscodingemail@gmail.com"  # Enter your address
receiver_email = "arysuri23@gmail.com"  # Enter receiver address
password = "Watson123"                  # Enter your email password
message = """
Subject: Reminder
"""

message += msg
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


print('Done')






#from email import message
#import smtplib, ssl
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

#to create html template for the email content
#from string import Template

#if we want images
#import base64

#Build email using html

#message = """
 #       <!DOCTYPE html>
 #          <html>
  #          <head>
   #           <title>Hello World !</title>
    #        </head>
     #      <footer style="background-color: gray;">
      #        <p style="text-align: center;">Contact us on : 
       #                      <a href="mailto:haaply.apps@gmail.com">
        #                     haaply.apps@gmail.com</a></p>
         #     </footer>
 #   </body>
  #</html>
#"""


# password = gmdjrbxtecskephs

#connect to the SMTP server
#s = smtplib.SMTP(host='smpt.gmail.com', port=587)
#s.starttls()

##login(sender email, sender password)
#.login('ahs8gup@virginia.edu', 'gmdjrbxtecskephs')

##msg = MIMEMultipart()

#setup paramaters of msg
#msg['From'] = 'ahs8gup@virginia.edu'
#msg['To'] = 'ahs8gup@virginia.edu'
#msg['Subject'] = 'Test'
#msg.attach(MIMEText(message, 'html'))

#send email
##s.send_message(msg)
#l msg

#s.quit()
#print('email sent')
