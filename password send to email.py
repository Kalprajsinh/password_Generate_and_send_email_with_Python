import random
import string
import smtplib

print("\nWelcome to rendom password Generat and email send with Python\n")
    
l = int (input("Enter length of password : "))
cha =  string.ascii_letters + string.punctuation + string.digits
x = random.sample(cha,l)
R = "".join(x)
print("Your password is Generated..\n")
name = input("Enter your name : ")
print()
receiver = input("Emter your Email id : ")

ob = smtplib.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("kalpraj51@gmail.com","##pasword##")
print("login success ...")

subject = "Password send using python "

j ="Hello ",name,",","\n\nYour generated password is : ",R,"\n\n\nThank You\nto use rendom password generate and Email send using python"
body ="".join(j)

message = "Subject:{}\n\n\n{}".format(subject,body)

ob.sendmail("kalpraj51@gmail.com",receiver,message)

print("Email send ...")
ob.quit()
