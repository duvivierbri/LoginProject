from tkinter import *

login = Tk()
login.propagate(0)
login.configure(background = "pink", width = 600, height = 400)
login.title("Just a lil project :) ~ Made by Brianna Duvivier")
login.resizable(width = False, height = False)

#What allows the button to print what was typed


def printit():
    global userbox
    global passbox
    global Username
    global Password
    global button
    global backbutton
    global Title
    global user
    global passw
    global usertext
    global passtext
    Username.destroy()
    Password.destroy()
    button.destroy()
    Title.destroy()
    passtext.destroy()
    usertext.destroy()
    Title = Label(login, text = "Is This Information Correct?", font = ("comic sans ms", 20), background = "pink")
    Title.place(x = 130, y = 100)
    user = a.get()
    passw = b.get()
    userbox = Label(login, text = ("Your Username Is Now: " + user), background = "pink", font = ("comic sans ms", 12))
    passbox = Label(login, text = ("Your Password Is Now: " + passw), background = "pink", font = ("comic sans ms",12))
    userbox.place(x = 150, y = 150)
    passbox.place(x = 150, y = 190)
    button = Button(login, width = 6, height = 1, text = "Confirm", command=loginpage)
    button.place(x = 450, y = 320)
    backbutton = Button(login, text = "Redo", width = 6, height = 1, command = tostartpage)
    backbutton.place(x = 90, y = 320)

a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()

Title = Label(login, text="Create A Username and Password", font = ("comic sans ms", 20), background = "pink")
Title.place(x = 80, y = 100)

Username = Entry(login, textvariable = a)
Username.place(x = 260, y = 200)

usertext = Label(login, text = "Set Username:", background = "pink")
usertext.place(x = 170, y = 197)

Password = Entry(login, textvariable = b)
Password.place(x = 260, y = 240)

passtext = Label(login, text = "Set Password:", background = "pink")
passtext.place(x = 170, y = 237)

button = Button(login, width = 6, height = 1, command = printit, text = "Done!")
button.place(x = 295, y = 270)

# FUNCTIONS

#Takes you back to the start page if you choose to redo the user and password
def tostartpage():
    global Title
    global userbox
    global passbox
    global backbutton
    global button
    global Username
    global Password
    global usertext
    global passtext

    userbox.destroy()
    passbox.destroy()
    usertext.destroy()
    passtext.destroy()
    Title.destroy()
    backbutton.destroy()
    button.destroy()
    Username.destroy()
    Password.destroy()
    
    Title = Label(login, text="Create A Username and Password", font = ("comic sans ms", 20), background = "pink")
    Title.place(x = 80, y = 100)

    Username = Entry(login, textvariable = a)
    Username.place(x = 260, y = 200)

    usertext = Label(login, text = "Set Username:", background = "pink")
    usertext.place(x = 170, y = 197)

    Password = Entry(login, textvariable = b)
    Password.place(x = 260, y = 240)

    passtext = Label(login, text = "Set Password:", background = "pink")
    passtext.place(x = 170, y = 237)

    button = Button(login, width = 6, height = 1, text = "Done!", command = printit)
    button.place(x = 295, y = 270)

#Takes you to login page after confirming information
def loginpage():
    global Title
    global button
    global backbutton
    backbutton.destroy()
    button.destroy()
    userbox.destroy()
    passbox.destroy()
    Title.destroy()
    Title = Label(login, text = "Okay, Now Log In!", font = ("comic sans ms", 20), background = "pink")
    Title.place(x = 190, y = 100)
    Username = Entry(login, textvariable = c)
    Password = Entry(login,textvariable = d)
    Username.place(x = 260, y = 170)
    Password.place(x = 260, y = 200)
    usertext = Label(login, text = "Username:", background = "pink")
    passtext = Label(login, text = "Password:", background = "pink")
    usertext.place(x = 190, y = 170)
    passtext.place(x = 190, y = 200)
    button = Button(login, width = 6, height = 1, text = "Login", command = match)
    button.place(x = 290, y = 240)

#Checks if username and password match
def match():
    global update
    update = Label(login)
    usermatch = False
    passmatch = False
    userlogin = c.get()
    passlogin = d.get()
    if (userlogin == user): #Username check
        usermatch = True
        update = Label(login, text = "       Usernames match       ", background = "pink")
        update.place(x = 180, y = 280)
    else:
        usermatch = False
        update = Label(login, text = "Usernames do not match", background = "pink")
        update.place(x = 180, y = 280)

    if (passlogin == passw): #Password check
        passmatch = True
        update = Label(login, text = "       Passwords match       ", background = "pink")
        update.place(x = 180, y = 310)
    else:
        passmatch = False
        update = Label(login, text = "Passwords do not match", background = "pink")
        update.place(x = 180, y = 310)

    if (usermatch == True) & (passmatch == True):
        update = Label(login, text = "       Congrats! Login Successful! :)                  ", background = "pink")
        update.place(x = 180, y = 340)
    else:
        update = Label(login, text = "Uh-Oh! Something went wrong. Try again.", background = "pink")
        update.place(x = 180, y = 340)


login.mainloop()
