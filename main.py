# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import tkinter
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
Font = ("Timesromannow",8, "bold")
window = tkinter.Tk()
window.title("Password Manager")
# window.minsize(200,200)
window.config(pady=50, padx=50, bg="lightsteelblue")

canvas = Canvas(width=200, height=200,bg="lightsteelblue", highlightthickness=0)  # Create a canvas
tomato_img = PhotoImage(file="logo.png")  # Load the tomato image
canvas.create_image(100, 100, image=tomato_img)  # Add the image to the canvas
canvas.grid(column=0, row=0, columnspan=2, sticky="e")  # Position the canvas in the grid


# lables
website_lable = Label(text="Website: ", font=Font, bg="lightsteelblue")
website_lable.grid(column=0, row=1)
email_lable = Label(text="Email/Username: ", font=Font, bg="lightsteelblue")
email_lable.grid(column=0, row=2)
password_lable = Label(text="Password: ", font=Font, bg="lightsteelblue")
password_lable.grid(column=0, row=3)


website_entry = Entry(window, width=38)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()
website_entry.delete(0,"end")
website_entry.insert(0, "")

email_entry = Entry(window, width=38)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "shiv@gmail.com")
# password generation

def password_generator():
    # Lists of possible characters for the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['*', '!', '$', '#', '@', '&', '%', '?']

    # Welcome message
    print("Welcome to the PyPassword Generator!")

    # User inputs for the number of each type of character


    # List to store password characters
    password = []
    # letters add
    letters_add = [choice(letters) for _ in range(randint(8,10))]
    # number add
    num_add = [choice(numbers) for _ in range(randint(2,4))]
    # Add random symbols to the password list
    symbols_add = [choice(symbols) for _ in range(randint(2,4))]

    # Shuffle the password list to randomize the order of characters
    password_list = letters_add + symbols_add + num_add
    shuffle(password_list)

    # Convert the list into a string to form the final password
    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)  # Copy the password to clipboard

# saving data
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="⚠️Error", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                  f"Email: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        with open("data.txt", "r") as file:
            print(file.read())

        # Clear the input fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


password_entry = Entry(window, width=19)
password_entry.grid(column=1, row=3, sticky="w")
#
generate_password_button = Button(text="Generate Password",command=password_generator, font=Font, width=15,bg="lightsteelblue", highlightthickness=0)
generate_password_button.grid(column=1, row=3, columnspan=3, sticky="E")  # Align to the right

add_button = Button(text="Add", font=Font,
                    command=save_data,
                    width=32, bg="lightsteelblue", highlightthickness=0)



add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()