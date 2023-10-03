import tkinter
import db
import dict


my_dict = dict.Dict(['fr'])
params = []

common_passwords_list = my_dict.get_passwords()
digit_list = my_dict.get_code_XXXX()
colors_list = ['Violet','Indigo','Bleu','Vert','Jaune','Orange','Rouge']
special_character = "#_&!-;"



print(common_passwords_list)
print(digit_list)
print(colors_list)
print(special_character)



my_db = db.DB()
my_db.create_table("user", ["login", "password"])
my_db.insert("user",
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

def generate_passwords(lists_to_combine):
    def recursive_combinations(lists, current_combination=[]):
        if not lists:
            return ["".join(current_combination)]

        current_list = lists[0]
        remaining_lists = lists[1:]

        combinations = []

        for item in current_list:
            new_combination = current_combination + [item]
            combinations.extend(recursive_combinations(remaining_lists, new_combination))

        return combinations

    all_combinations = recursive_combinations(lists_to_combine)

    return all_combinations

def clicked():
    open('./src/all_password_combinaisons.txt', 'w').write('\n'.join(generate_passwords(params)))




def common_passwords_selection():
    if common_passwords_var.get() == 1:
        params.append(common_passwords_list)
    
def digits_selection():
    if digits_var.get() == 1:
        params.append(digit_list)

def colors_selection():
    if colors_var.get() == 1:
        params.append(colors_list)

def special_selection():
    if special_var.get() == 1:
        params.append(special_character)  

window = tkinter.Tk()
window.title("Brut force password app / tp SIO ")
window.geometry('500x400')

input_frame = tkinter.Frame(window)
input_frame.pack()
lbl = tkinter.Label(input_frame, text="Hello")
lbl.grid(column=0, row=0)

e = tkinter.Entry(input_frame)
e.grid(column=0, row=1)

common_passwords_var = tkinter.IntVar()
common_passwords = tkinter.Checkbutton(input_frame, text='commons', variable=common_passwords_var, onvalue=1, offvalue=0, command=common_passwords_selection)
common_passwords.grid(column=0, row=2)

digits_var = tkinter.IntVar()
digits = tkinter.Checkbutton(input_frame, text='digits', variable=digits_var, onvalue=1, offvalue=0, command=digits_selection)
digits.grid(column=1, row=2)

colors_var = tkinter.IntVar()
colors = tkinter.Checkbutton(input_frame, text='colors', variable=colors_var, onvalue=1, offvalue=0, command=digits_selection)
colors.grid(column=2, row=2)

special_var = tkinter.IntVar()
special = tkinter.Checkbutton(input_frame, text='specials', variable=special_var, onvalue=1, offvalue=0, command=special_selection)
special.grid(column=3, row=2)

btn = tkinter.Button(input_frame, text="Click Me", command=clicked)
btn.grid(column=0, row=3)



window.mainloop()








