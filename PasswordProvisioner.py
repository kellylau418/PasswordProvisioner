from tkinter import *
from tkinter.messagebox import *
from tkinter import _setit
import string
import random
import tkinter.ttk



def save_password():
    global service_list, uname_list, password_list
    service = service_var.get()
    uname = uname_var.get()
    password = password_var.get()

    if service in service_list:
        chosen = service_list.index(service)
        uname_list[chosen] = uname
        password_list[chosen] = password
        showinfo("Updated!", "Your new service, username, and password have been updated.")
    
    else:
        service_list.append(service)
        uname_list.append(uname)
        password_list.append(password)
        service_option['menu'].add_command(label=service, command=_setit(service_option_var, service))
        showinfo("Saved!", "Your new service, username, and password have been saved.")

    service_var.set("")
    uname_var.set("")
    password_var.set("")
    print(service_list)
    print(uname_list)
    print(password_list)

    strength_password(password)
    
def strength_password(some_pw):

    pt = determine_password_strength(some_pw)

    strength_var.set(pt)

    if pt <= 4:
        s_label_var.set("Complexity Level: WEAK")
        strength_scale.config(troughcolor="#00FF00")
        strength_scale.config(fg="#276746")
        strengh_label.config(fg="#276746")


    elif pt <=7:
        s_label_var.set("Complexity Level: MEDIUM")
        strength_scale.config(troughcolor="#FFFF00")
        strength_scale.config(fg="#EEA841")
        strengh_label.config(fg="#EEA841")

    elif pt <=10:
        s_label_var.set("Complexity Level: STRONG")
        strength_scale.config(troughcolor="#FF0000")
        strength_scale.config(fg="#A30A35")
        strengh_label.config(fg="#A30A35")
    
def determine_password_strength(some_password):
    points = 0
    
    if len(some_password) >= 8:
        points += 2
        print("b")
    if count_occurrences(some_password, string.ascii_lowercase) >= 2:
        points += 2
    if count_occurrences(some_password, string.ascii_uppercase) >= 2:
        points += 2
    if count_occurrences(some_password, string.digits) >= 2:
        points += 2
    if count_occurrences(some_password, string.punctuation) >= 2:
        points += 2

    return points


def count_occurrences(word, possible_characters):

    count = 0
    for char in word:
        if char in possible_characters:
            count += 1
    return count


def show_info():
    chosen_service = service_option_var.get()
    if chosen_service in service_list:
        chosen_index = service_list.index(chosen_service)
    chosen_uname = uname_list[chosen_index]
    chosen_pw = password_list[chosen_index]

    show_uname_var.set(f'Retrived Username: {chosen_uname}')
    show_pw_var.set(f'Retrived Password: {chosen_pw}')


def make_new_password():    
    new_password = ''
    lower = lower_var.get()
    upper = upper_var.get()
    digit = digit_var.get()
    symbols = symbols_var.get()

    #ADD CODE HERE TO ADD APPROPRIATE CHARACTERS TO new_password
    if lower == 1:
        
        a = random.choice(string.ascii_lowercase)
        b = random.choice(string.ascii_lowercase)
        print(a,b)
        new_password += a
        new_password += b

    if upper == 1:
        a = random.choice(string.ascii_uppercase)
        b = random.choice(string.ascii_uppercase)

        new_password += a
        new_password += b

    if digit == 1:
        a = random.choice(string.digits)
        b = random.choice(string.digits)

        new_password += a
        new_password += b

    if symbols == 1:
        a = random.choice(string.punctuation)
        b = random.choice(string.punctuation)

        new_password += a
        new_password += b


    
    new_password = list(new_password)
    random.shuffle(new_password)
    new_password = ''.join(new_password)

    password_var.set(new_password)
    strength_password(new_password)

def password_visibility():
    state = visibility_var.get()
    pw = password_var.get()

    if state == "Show":
        password_entry.grid(row=4, column=2, sticky=W)
        password_label.grid(row=4, column=1, sticky=W)

    else:

        password_entry.grid_forget()
        password_label.grid_forget() 
    
#main
global service_list, uname_list, password_list
service_list = ['gmail', 'spotify', 'games.com']
uname_list = ['somebody', 'sombody_s', 'my name is']
password_list = ['Abc#rST&19E', 'abc123', 'G^bh']

print(service_list)
print(uname_list)
print(password_list)

root = Tk()
mainframe = Frame(root)

#create widgets
title_label = Label(mainframe, font=('Academy Engraved LET', 30), text="Password Manager")

service_label = Label(mainframe, font=('Baskerville',20), text="Service:", fg="#28417A")
service_var = StringVar()
service_entry = Entry(mainframe, width=20, font=('Baskerville',15), fg="#4073FF", textvariable=service_var)

uname_label = Label(mainframe, font=('Baskerville',20), text="Username:", fg="#28417A")
uname_var = StringVar()
uname_entry = Entry(mainframe, width=20, font=('Baskerville',15), fg="#4073FF", textvariable=uname_var)

password_label = Label(mainframe, font=('Baskerville',20), text="Password:", fg="#28417A")
password_var = StringVar()
password_entry = Entry(mainframe, width=20, font=('Baskerville',15), fg="#4073FF", textvariable=password_var)

save_button = Button(mainframe, text="Save", font=('Academy Engraved LET',25), fg="#28417A", command=save_password) 

strength_var = IntVar()
strength_var.set(0)
strength_scale = Scale(mainframe, from_=0, to=10, variable=strength_var, width=20, length=150, font=('Baskerville', 15), orient=HORIZONTAL, showvalue=True, state=DISABLED)

s_label_var = StringVar()
s_label_var.set("Complexity Level:")
strengh_label = Label(mainframe, font=('Academy Engraved LET',15), textvariable=s_label_var)

show_uname_var = StringVar()
show_uname_label = Label(mainframe, font=('Academy Engraved LET',20), text="Username:", textvariable=show_uname_var)

show_pw_var = StringVar()
show_pw_label = Label(mainframe, font=('Academy Engraved LET',20), text="Password:", textvariable=show_pw_var)

service_option_var = StringVar()
service_option_var.set("gmail")
service_option = OptionMenu(mainframe, service_option_var, *service_list)
service_option.config(font=('Academy Engraved LET',15), fg="#006400")

show_button = Button(mainframe, text="Show Username and Password", fg="#006400", font=('Academy Engraved LET',15), command=show_info)

grouprandom = LabelFrame(mainframe, text="Generate Password", font=('Academy Engraved LET',20), fg="#4B0082")

lower_var = IntVar()
lower_check = Checkbutton(grouprandom, text="Lowercase Letters", font=('Baskerville',15), variable=lower_var, onvalue=1, offvalue=0, fg="#8A2BE2")

upper_var = IntVar()
upper_check = Checkbutton(grouprandom, variable=upper_var, text="Uppercase Letters", font=('Baskerville',15), onvalue=1, offvalue=0, fg="#8A2BE2")

digit_var = IntVar()
digit_check = Checkbutton(grouprandom, variable=digit_var, text="Digits", font=('Baskerville',15), onvalue=1, offvalue=0, fg="#8A2BE2")

symbols_var = IntVar()
symbols_check = Checkbutton(grouprandom, variable=symbols_var, text="Punctuation/Symbols", font=('Baskerville',15), onvalue=1, offvalue=0, fg="#8A2BE2")

generate_button = Button(grouprandom, text="Generate", font=('Baskerville',15), command=make_new_password, fg="#4B0082")

visibility_frame = LabelFrame(mainframe, text="Password Entry Visibility", font=('Academy Engraved LET',20), fg="#008080")

visibility_var = StringVar()
visibility_var.set("Show")
show_radio = Radiobutton(visibility_frame, text="Show", variable=visibility_var, font=('Baskerville',15), value="Show", command=password_visibility, fg="#48D1CC")
disappear_radio = Radiobutton(visibility_frame, text="Disappear", variable=visibility_var, font=('Baskerville',15), value="Disappear", command=password_visibility, fg="#48D1CC")


#Grid widgets

mainframe.grid(padx = 80, pady=50)

title_label.grid(row=1, column=1, sticky=W, pady=20, columnspan=3)

service_label.grid(row=2, column=1, sticky=W)
service_entry.grid(row=2, column=2, sticky=W)

uname_label.grid(row=3, column=1, sticky=W)
uname_entry.grid(row=3, column=2, sticky=W)

password_label.grid(row=4, column=1, sticky=W)
password_entry.grid(row=4, column=2, sticky=W)

save_button.grid(row=5, column=1, rowspan=2, pady=30, ipadx=10, ipady=5, sticky=W)

strength_scale.grid(row=6, column=2, padx=20, sticky=NW)
strengh_label.grid(row=5, column=2, padx=20, sticky=SW)

service_option.grid(row=8, column=1, sticky=EW)
show_button.grid(row=8, column=2, sticky=W)
show_uname_label.grid(row=9, column=1, columnspan=3, sticky=W)
show_pw_label.grid(row=10, column=1, columnspan=3, sticky=W)

grouprandom.grid(row=2, column=4, rowspan=3, sticky=W, padx=50)
lower_check.grid(sticky=W)
upper_check.grid(sticky=W)
digit_check.grid(sticky=W)
symbols_check.grid(sticky=W)
generate_button.grid(sticky=W)

visibility_frame.grid(row=8, column=4, sticky=W, padx=50)
show_radio.grid(sticky=W)
disappear_radio.grid(sticky=W)

tkinter.ttk.Separator(mainframe, orient=VERTICAL).grid(row=2, column=3, rowspan=8, sticky='ns', padx=10)
tkinter.ttk.Separator(mainframe, orient=HORIZONTAL).grid(row=7, column=1, columnspan=8, sticky='we', pady=10)

root.mainloop()
