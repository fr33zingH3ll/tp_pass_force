from dict import Dict
from db import DB

country = Dict(['fr','pt','gb'])
prefix = "XXXX"

### partie 1 ###
################

db = DB()
db.create_table("user", ["login", "password"])
db.insert("user",
    {
    "champs":["login","password"],
    "values":[
        ['Bob','123456'],
        ['Tom','azerty'], 
        ['Tim','marseille1993'], 
        ['Kay','dauphinBleu'], 
        ['Zed','dragon42'], 
        ['May','naruto#7']
    ]
})
print('PART 1')
all_users = db.get_all("user")
print(all_users)
print('---------------------------------------')

### partie 2 ###
################

print('PART 2')
my_dicts = Dict(['fr','gb','pt'])
passwords_list = my_dicts.get_passwords()
print(passwords_list)
print('---------------------------------------')

### partie 3 ###
################

print("PART 3")
for user in all_users:
    if user[1] in passwords_list:
        print(f"password {user[1]} is in the common list password")
print('---------------------------------------')

### partie 4 ###
################

print("PART 4")
list_number = my_dicts.get_code_XXXX()
# Initialisez une nouvelle liste pour stocker les mots de passe avec le numéro de 0000 à 9999
new_passwords_list = []

# Itérez sur chaque mot de passe dans la liste initiale
for password in passwords_list:
    # Générez différentes combinaisons en ajoutant un numéro de 0000 à 9999
    for num in range(10000):
        # Créez un mot de passe potentiel en ajoutant le numéro actuel (zéro complété à 4 chiffres)
        potential_password = f"{password}{num:04}"
        new_passwords_list.append(potential_password)

for user in all_users:
    if user[1] in new_passwords_list:
        print(f"password {user[1]} is in the common list password")
print('---------------------------------------')