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


assignments = {}
a = "Y"
while(a == "Y"):
    name = input("What is the name of your assignment?")
    year = input("What year is this assignment due?")
    month = input("What month is this assignment due?")
    day = input("What day is this assignment due?")
    assignments[name] = date(int(year), int(month), int(day))
    a = input("Would you like to enter another assignment? Enter Y or N?")

print(assignments)

'''
assignments = {
    'Psych Chapter One' : date(2021, 8, 29),
    'CS 3330 Quiz' : date(2021, 9, 1),
    'Stat 3080 project' : date(2021, 9, 3),
    'Technosonics compo': date(2021, 9, 18),
    'Stat 2120 HW' : date(2021, 10, 10)

    #follow format to continue to add more

}
'''
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
sender_email = "aryscodingemail@gmail.com"  # Enter sender address
receiver_email = "...@gmail.com"  # Enter receiver address
password = "..."                  # Enter your email password
message = """
Subject: Reminder
"""

message += msg
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


print('Done')




