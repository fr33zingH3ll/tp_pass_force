import random

def test2string(string_1, string_2):
    return string_1 == string_2

def test_pass_force(dict, list, dict_opt = False):
    

    for key, value in dict.items():
        list_pass_forced = []
        print(f"dictionaire_{key}")
        with open(f"dictionnaire_{key}.txt", "r") as file:
            for password in file:
                password = password.split('\n')
                if dict_opt != None:
                    with open("number.txt", "r") as number_file:
                        for number in number_file:
                            number = number.split('\n')
                            password += str(number[0])
                            for item in list:
                                if item == password[0]:
                                    print(f"{item} = {password[0]}")    
                else:
                    for item in list:
                        if item == password[0]:
                            print(f"{item} = {password[0]}")
        print('------------------------------------------------')

def addXXXXrandom(tuple):
    new_list = []
    string = ""
    numbers = [random.randint(0,9) for i in range(4)]

    for item in tuple:
        string = item[1]
        for number in numbers:
            string += str(number)
        new_list.append(string)
    return string