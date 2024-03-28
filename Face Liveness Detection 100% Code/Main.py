import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

from tkinter import messagebox as ms

##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('r.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#


label_l1 = tk.Label(root, text="!!!___Welcome To System___!!!",font=("Times New Roman", 35, 'bold'),
                    background="black", fg="white", width=30, height=1)
label_l1.place(x=300, y=300)




    
# def window():
#   root.destroy()


# button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="lightblue", fg="black")
# button1.place(x=100, y=240)

# button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="lightblue", fg="black")
# button2.place(x=100, y=320)

# button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=100, y=400)

root.mainloop()

