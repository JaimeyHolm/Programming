def new_password(oldpassword, newpassword):
    return newpassword != oldpassword and len(newpassword) >= 6


oldpassword = input('Wat is je oude wachtwoord? ')
newpassword = input('Wat is je nieuwe wachtwoord? ')

x = new_password(oldpassword, newpassword)

print (x)