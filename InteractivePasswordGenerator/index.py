import random
import time 

#Title 

print("----------STRONG PASSWORD GENERATOR!----------")
print("")

#The alert message 

time.sleep(1)
print("The min it's 12 and the max it's 40")
print("")

#The caracteries 

abc = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
symbols = "!@#$%()[]"

#The sizes...

password_size_max = 40
password_size_min = 12

#Input of password 

change_password_size = int(input("Please put the size of password > "))

#The generator...

if change_password_size <= password_size_max and change_password_size >= password_size_min:
    
    password_addition = abc + num + symbols
    password = "".join(random.sample(password_addition,change_password_size))
    print("Your password: {}".format(password))

#While the password is too small 

while password_size_min > change_password_size:

    password_remake_min = int(input("Put a password with 12 caracteries or more > "))

    if password_remake_min >= password_size_min:
     password_addition = abc + num + symbols
     password = "".join(random.sample(password_addition,password_remake_min))
     print("Your password: {}".format(password))
     
    break

#While the password is too large

while change_password_size > password_size_max:
    password_remake_max = int(input("The max caracteries it's 40! > "))

    if password_size_max >= password_remake_max:
 
     password_addition = abc + num + symbols
     password = "".join(random.sample(password_addition,password_remake_max))
     print("Your password: {}".format(password))

     break 

#Final decoration

print("")
print("----------------------------------------------")

    

    

