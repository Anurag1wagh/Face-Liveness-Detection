
import os,math # Text accept
import random,sys # to generate random float value
import smtplib #Important Statement use 
#import os
from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk     
from PIL import Image 

from tkinter import messagebox as ms
Window=Tk()
Window.geometry("620x320")
Window.title("MAIL OTP")
w, h = Window.winfo_screenwidth(), Window.winfo_screenheight()
#Window.geometry("%dx%d+0+0" % (w, h))
#------------------------
image2 =Image.open('1.png')
image2 =image2.resize((620,320), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label =Label(Window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
a=IntVar()
#--------------------------------------------------------
def verify():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)
    
    mailid= cmd
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
    # s.login("sheetal09.srccode@gmail.com", " ")
    # print(msg)
    # s.sendmail('sheetal09.srccode@gmail.com',mailid,msg)

    mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
    mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls() #security connection
    mail.login('wanurag61@gmail.com',' islcdtmishajzpsw') #login part
    mail.sendmail('sagargaikwad4253@gmail.com',mailid,msg) #send part

    os.system('python second.py')
label1=Label(Window,text="One Time Password",relief="solid",font=("arial",26,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="EMAIL ID",font=("arial",15,"bold"),width=20).place(x=50,y=100)
w=Entry(Window,width=20,validate="key",textvariable=a,font=("arial",15,"bold"))
w.place(x=320,y=100)

log = Button(Window, text="Proceed",relief="raised", bg='maroon', font=("arial", 22, "bold"), fg='black',command=verify).place(x=250,y=190)
Window.mainloop()