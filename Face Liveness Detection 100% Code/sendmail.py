

import os,math# Python madhle je kahi text ahet to accept karto
import random,sys#To generate random float value
import smtplib#Import statement
#mailid= cmd
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg='Your OTP Verification for app is '+OTP+' Note..  Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid'
file2=open("otp.txt","w")
file2.write(OTP)
file2.close()

# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login("wanurag61@gmail.com", "islcdtmishajzpsw")
# print(msg)
# s.sendmail('sagargaikwad4253@gmail.com',mailid,msg)

mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
mail.starttls() #security connection
mail.login('wanurag61@gmail.com',' islcdtmishajzpsw') #login part
mail.sendmail('sagargaikwad4253@gmail.com',msg) #send part

os.system('python second.py')