import ctypes
import json

# Enable High-DPI awareness for clearer graphics on Windows
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from random import *  # Import all functions from random (can lead to namespace conflicts)
import ttkbootstrap as ttk  # ttkbootstrap provides modern themed widgets for Tkinter
from ttkbootstrap.constants import *  # Import layout constants like LEFT, RIGHT, etc.
import pyperclip  # To copy password directly to clipboard
from tkinter import messagebox  # Message box for alerts
from tkinter import PhotoImage  # For loading images like the logo

# ---------------------------- UI SETUP ------------------------------- #

# Set font for labels
Font = ("Times New Roman", 9, "bold")

# Create main window with ttkbootstrap's "superhero" theme
window = ttk.Window(themename="superhero")
window.title("Password Manager")
window.config(pady=50, padx=50)  # Add padding around the window

# Logo setup
canvas = ttk.Canvas(window, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")  # Load logo image (ensure logo.png exists in the directory)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# ---------------------------- LABELS ------------------------------- #
# Label for website field
website_label = ttk.Label(window, text="Website:", font=Font)
website_label.grid(column=0, row=1, sticky="w")

# Label for email/username field
email_label = ttk.Label(window, text="Email/Username:", font=Font)
email_label.grid(column=0, row=2, sticky="w")

# Label for password field
password_label = ttk.Label(window, text="Password:", font=Font)
password_label.grid(column=0, row=3, sticky="w")

# ---------------------------- ENTRY FIELDS ------------------------------- #
# Entry for website input
website_entry = ttk.Entry(window, width=17)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()  # Focus cursor on website entry

# Entry for email/username input
email_entry = ttk.Entry(window, width=36)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "imuniqueshiv@gmail.com")  # Default email

# Entry for password input
password_entry = ttk.Entry(window, width=17)
password_entry.grid(column=1, row=3, sticky="w")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Lists of possible characters for the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['*', '!', '$', '#', '@', '&', '%', '?']

    # Generate random characters for the password
    letters_add = [choice(letters) for _ in range(randint(8, 10))]  # 8-10 random letters
    num_add = [choice(numbers) for _ in range(randint(2, 4))]       # 2-4 random numbers
    symbols_add = [choice(symbols) for _ in range(randint(2, 4))]   # 2-4 random symbols

    # Combine all characters and shuffle them
    password_list = letters_add + symbols_add + num_add
    shuffle(password_list)  # Shuffle for randomness

    # Convert the list to a string and insert it into the password entry field
    final_password = "".join(password_list)
    password_entry.insert(0, final_password)  # Insert into entry box
    pyperclip.copy(final_password)  # Copy to clipboard

# ---------------------------- SAVE FUNCTION ------------------------------- #
def save_data():
    # Get user input from entry fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if any field is empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="⚠️ Error", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try to read existing data from the JSON file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Load existing data
        except FileNotFoundError:
            # If file doesn't exist, initialize an empty dictionary
            data = {}
        # Update the data with new entries
        data.update(new_data)
        # Write updated data back to the JSON file
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)  # Write updated data to the file
        # Show success message and clear input fields
        messagebox.showinfo(title="Success", message="Data saved successfully.")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD FUNCTION ------------------------------- #
def find_password():
    # Get the website name from the entry field
    website = website_entry.get()
    try:
        # Try to read existing data from the JSON file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)  # Load existing data
    except FileNotFoundError:
        # Show error if the file doesn't exist
        messagebox.showerror(title="⚠️ Error", message="No data file found.")
        return
    # Check if the website exists in the data
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        # Show the email and password for the website
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        # Show error if no details exist for the website
        messagebox.showerror(title="⚠️ Error", message="No details for the website exists.")
    # Clear the input fields
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- BUTTONS ------------------------------- #
# Button to search for a password
search_button = ttk.Button(window, text="Search", command=find_password, width=16, bootstyle="info")
search_button.grid(column=2, row=1, sticky="w")

# Button to generate a random password
generate_password_button = ttk.Button(window, text="Generate Password",
                                      command=password_generator, width=16, bootstyle="primary")
generate_password_button.grid(column=2, row=3, sticky="w")

# Button to save the data
add_button = ttk.Button(window, text="Add", command=save_data, width=35, bootstyle="success")
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

# Run the application
window.mainloop()
