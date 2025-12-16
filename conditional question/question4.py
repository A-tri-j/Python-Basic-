# passWord Strength checker

password=(input("Give me a password : "))

if len(password)<6:
    strength ="Weak"

if len(password)<=10:
    strength ="Medium"
else:
    strength ="Strong"


print ("Password Strength is : ", strength)
