from tkinter import *  # * imports all the classes
from tkinter import messagebox  # messagebox is a module not a class
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # using list comprehension
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    # pop up message
    if len(website) == 0 or len(password) == 0:
        # messagebox is used to display a pop up message
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        # pop up message
        is_ok = messagebox.askokcancel(
            "ALERT!", "Do you want to save this password?\n")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                input_website.delete(0, END)
                input_password.delete(0, END)
        else:
            input_website.delete(0, END)
            input_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas_image = Canvas(width=200, height=200)
locker_image = PhotoImage(file="logo.png")
# width and height will be half of the canvas width and heigth
canvas_image.create_image(100, 100, image=locker_image)
canvas_image.grid(column=1, row=1)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=3)

input_website = Entry(width=35)
input_website.focus()
input_website.grid(column=1, row=3)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=4)

input_email = Entry(width=35)
# insert takes 2 parameters index and string
input_email.insert(0, "KunjMaheshwari@gmail.com")
input_email.grid(column=1, row=4)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=5)

input_password = Entry(width=17)
input_password.grid(column=1, row=5)

Generate_password = Button(text="Generate Password", command=generate)
Generate_password.grid(column=2, row=5)

Add_Button = Button(text="Add", width=35, command=save)
Add_Button.grid(column=1, row=6)


window.mainloop()
