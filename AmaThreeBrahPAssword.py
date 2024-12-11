import tkinter as tk_
import time as tim_
import datetime as dtim_

usernameAmathuba = input("Enter your Amathuba Username: ")
passwordAmathuba = input("Enter your Amathuba Password: ")

currentTime = dtim_.datetime.now()

# Check for first 6 letters
txt_uName = usernameAmathuba.split()
#if (txt_uName[0] or txt_uName[1]) != int
print(txt_uName, " is the list")

# PRINT ALL
print("Welcome back,", usernameAmathuba)
print("Your password is:",passwordAmathuba)



for i in range(3):
    print(currentTime, " haaH")
