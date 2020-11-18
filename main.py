import calendar
from easygui import *

f = open("test.csv", 'a')
k = open("test.txt", 'a')

# Personal information
firstname = input("What is your firstname?: ")
f.write(f"Name: {firstname}\n")

surname = input("What is your lastname?: ")
f.write(f"Name: {surname}\n")

age = int(input("What is your age?: "))
f.write(f"Age: {age}\n")

# message to be displayed
textGender = "What is your gender?"
# window title
titleGender = "Gender"
# item choices
choicesGender = ["Male", "Female", "Other"]
# creating a button box
output = choicebox(textGender, titleGender, choicesGender)
# title for the message box
title = "Message Box"
# message
messageGender = str(output)
# creating a message box
# msg = msgbox(messageGender, title)
# messageGender = input(str(output))
f.write(f"Gender: {messageGender}\n")

country = input("Which country do you live in?: ")
f.write(f"Country: {country}\n")
city = input("Which city do you live in?: ")
f.write(f"City: {city}\n")

# Contact information
phoneNumber = int(input("What is your phone number?: "))
f.write(f"Phone number: {phoneNumber}\n")
eMail = input("What is your E-Mail?: ")
f.write(f"E-mail: {eMail}\n")

# Physical information
Height = int(input("How tall are you in centimeters?: "))
f.write(f"Height in cm :{Height}\n")
Weight = int(input("How much do you weigh in kilograms?: "))
f.write(f"Weight in Kg: {Weight}\n")

# Health Issues
# Smoke = input("Do you smoke? If yes, please specify how many cigarettes you approximately smoke per day: ")
# message to be displayed
textSmoke = "Do you smoke? If yes, how much do you smoke?"
# window title
titleSmoke = "Smoke"
# item choices
choicesSmoke = ["No", "Occasional smoker (1-2 weekly)", "Party smoker (2-5 weekly)", "Light (8-12 daily)",
                "Heavy smoker(20+ daily)"]
# creating a button box
output = choicebox(textSmoke, titleSmoke, choicesSmoke)
# title for the message box
title = "Message Box"
# message
messageSmoke = str(output)
# creating a message box
# msg = msgbox(messageSmoke, title)
f.write(f"Smoke: {messageSmoke}\n")

# Diabetes = input("Do you have any sort/type of diabetes?: ")
# message to be displayed
textDiabetes = "Do you have any sort/type of diabetes?"
# window title
titleDiabetes = "Diabetes"
# item choices
choicesDiabetes = ["Type 1", "Type 2", "Gestational", "No"]
# creating a button box
output = choicebox(textDiabetes, titleDiabetes, choicesDiabetes)
# title for the message box
title = "Message Box"
# message
messageDiabetes = str(output)
# creating a message box
# msg = msgbox(messageDiabetes, title)
f.write(f"Diabetes?: {messageDiabetes}\n")

# Hypertension = input("Do you have Hypertension?: ")
# message to be displayed
textHP = "Do you have Hypertension??"
# window title
titleHP = "Hypertension"
# item choices
choicesHP = ["Yes", "No"]
# creating a button box
output = choicebox(textHP, titleHP, choicesHP)
# title for the message box
title = "Message Box"
# message
messageHP = str(output)
# creating a message box
# msg = msgbox(messageHP, title)
f.write(f"Hypertension?: {messageHP}\n")

# CardiacDiseases = input("Do you have any cardiac diseases?: ")
# message to be displayed
textCD = "Do you have any cardiac diseases?"
# window title
titleCD = "Cardiac Diseases"
# item choices
choicesCD = ["Yes", "No"]  # skal vi have et input, hvor brugeren kan specify??
# creating a button box
output = choicebox(textCD, titleCD, choicesCD)
# title for the message box
title = "Message Box"
# message
messageCD = str(output)
# creating a message box
# msg = msgbox(messageCD, title)
f.write(f"Cardiac Diseases?: {messageCD}\n")

other = input("Do you have any other conditions?: ")
f.write(f"Other condition?: {other}\n")

# Surgical area of interest
# Operation = input("Which area of your body do you wished to have changed? please specify: ")
# message to be displayed
textAoE = "Which area of your body do you wished to have changed?"
# window title
titleAoE = "Surgical area of interest"
# item choices
choicesAoE = ["Face", "Neck", "Nose", "Eyelid", "Eyebrow", "Hand", "Arm", "Breast", "Abdomen", "Thigh",
              "Body Sculpture", "Reconstructive surgeries", "other"]
# creating a button box
output = choicebox(textAoE, titleAoE, choicesAoE)
# title for the message box
title = "Message Box"
# message
messageAoE = str(output)
# creating a message box
# msg = msgbox(messageAoE, title)
f.write(f"Surgical area of interest: {messageAoE}\n")

otherAoe = input("Which other surgical area of interest do you have?: ")
f.write(f"Other surgical are of interest is: {otherAoe}\n")

# Contact information
print("We can have our online consultation in WhatsApp, Instagram, Skype, Zoom, or Facebook Messenger.")
# Platform = input("In which platform, do you wish to have the consultation?")
textPlatform = "Which area of your body do you wished to have changed?"
# window title
titlePlatform = "Surgical area of interest"
# item choices
choicesPlatform = ["WhatsApp", "Instagram", "Skype", "Zoom", "Facebook Messenger"]
# creating a button box
output = choicebox(textPlatform, titlePlatform, choicesPlatform)
# title for the message box
title = "Message Box"
# message
messagePlatform = str(output)
# creating a message box
# msg = msgbox(messagePlatform, title)
f.write(f"Platform: {messagePlatform}\n")

OnlineConsultation = input("What is your account information on this platform?: ")
f.write(f"Platform: {OnlineConsultation}\n")

print("The calendar for the year 2021 is: " + calendar.calendar(2021, 2, 1, 6))
Date = int(input("Please have a look at the calendar, and choose a date for the online consultation: YYYY-MM-DD "))
f.write(f"date: {Date}\n")


# if date is true
#   set date
# print("please specify your wished time, then i'll get back to you about the specific time")


# root = tk()
# root.title("Calendar")

# cal = calendar(root, selectmode="day", year=2021, month=5, day=22)
# cal.pack(pady=21)


# def grab_date():
#   my_label.config(text=cal.get_date())


# my_button = tk.Button(root, text="Get Date", command=grab_date)
# my_button.pack(pady=21)

# my_label = label(root, text="")
# my_label.pack(pady=21)

# root.mainloop()
