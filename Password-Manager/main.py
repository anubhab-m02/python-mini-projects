from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Lists of characters to generate a password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random characters for password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle characters to create the final password
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # Insert generated password into the entry field and copy to clipboard
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # Retrieve data from entry fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create a dictionary for new data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if required fields are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Dayummm!", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try to open existing data file
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # If the file doesn't exist, create a new one with the new data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear entry fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    # Retrieve website from the entry field
    website = website_entry.get()
    try:
        # Try to open the data file
        with open("data.json") as data_file:
            # Load data from the file
            data = json.load(data_file)
    except FileNotFoundError:
        # Show an error message if the file doesn't exist
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # Check if the website is in the data
        if website in data:
            # Retrieve email and password for the website and display them
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # Show an error message if no details for the website exist
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for displaying logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Password-Manager\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)

# Labels for entry fields
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields for website, email, and password
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, padx=5, pady=5)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
email_entry.insert(0, "anubhab.m248@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons for searching, generating passwords, and saving
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2, pady=5)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=5)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=0, columnspan=3, pady=20)

window.mainloop()