import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    generated = "".join(password_list)
    Pass_entry.insert(0, generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = website_entry.get()
    username = email_entry.get()
    password = Pass_entry.get()
    new_data = {website: {"email": username, 'password':password}}
    if website == "" or username == "" or password == "":
        messagebox.showerror(title='Error', message="You have left the necessary fields empty")

    else:
        pyperclip.copy(password)
        data = {}
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        website_entry.delete(0, END)
        Pass_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():
    search_input = website_entry.get()
    with open('data.json', 'r') as file:
        data = json.load(file)
    if search_input in data.keys():
        details = data[search_input]
        messagebox.showinfo(title=f'{search_input}', message=f"Email:{details['email']}\nPassword:{details['password']}")
    else:
        messagebox.showerror(title='Notfound', message='No such website found!')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=20)

img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text='Search', command=search, width=12)
search_button.grid(row=1, column=2)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "your_email@email.com")

Pass_label = Label(text='Password:')
Pass_label.grid(row=3, column=0)

Pass_entry = Entry(width=20)
Pass_entry.grid(row=3, column=1)

Generate_button = Button(text='Generate Password', command=password)
Generate_button.grid(row=3, column=2)

ADD_button = Button(text='Add', width=36, command=add)
ADD_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
