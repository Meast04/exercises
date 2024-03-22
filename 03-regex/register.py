import re
users = {}
def validate_password(password):
    return re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(.{8})",password)



def register():
    username = input("Geef mij username:")
    password = input("Geef mij password:")
    if validate_password(password):
        users[username] = password
        print("Succesvol geregistreerd")

    else : 
        print("Zorg dat uw wachtwoord de nodige voorwaarden heeft:")



register()
print(users)




