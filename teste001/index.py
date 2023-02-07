import random
import time 

#Title 

print("----------STRONG PASSWORD GENERATOR!----------")
print("")

time.sleep(1)
print("The min it's 12 and the max it's 40")


#The caracteries 

abc = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
symbols = "!@#$%()[]"

#The sizes...

password_size = 12
password_size_max = 40
password_size_min = 10

#Input of password 

change_password_size = int(input("Please put the size of password > "))


#The generator...

if change_password_size < password_size_max or change_password_size > password_size_min:

    password_size = change_password_size 
    password_addition = abc + num + symbols
    password = "".join(random.sample(password_addition,password_size))
    print("Your password: {}".format(password))

elif change_password_size > password_size_max:
    print("ERROR! to large password!")

elif change_password_size < password_size_min:
    print("'\033[31m0' to small password")

else:
    print("A unknown error appened")

#CORRIGIR AMANHÃ 


"""
#size

password_size = 12
password_addition = abc + num + symbols

#Make the password 

password = "".join(random.sample(password_addition,password_size))

#Password print

print("Your password: {}".format(password))



#Final decoration

print("")
print("----------------------------------------------")
"""