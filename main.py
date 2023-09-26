
from part_1 import *
from part_3 import *
from dict import Dict
from db import DB

country = Dict(['fr','pt','gb'])

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
db.get_all("user")


### partie 2 ###
################

### partie 3 ###
################



    
