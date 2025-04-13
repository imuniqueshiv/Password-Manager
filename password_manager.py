import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)  # High-DPI awareness for clearer graphics on Windows

from random import *  # Imports all functions from random (can lead to namespace conflicts)
import ttkbootstrap as ttk  # ttkbootstrap provides modern themed widgets for Tkinter
from ttkbootstrap.constants import *  # Imports layout constants like LEFT, RIGHT, etc.
import pyperclip  # To copy password directly to clipboard
from tkinter import messagebox  # Message box for alerts
from tkinter import PhotoImage  # For loading images like the logo

# ---------------------------- UI SETUP ------------------------------- #

Font = ("Times New Roman", 9, "bold")  # Set font for labels

# Create main window with ttkbootstrap's "superhero" theme
window = ttk.Window(themename="superhero")
window.title("Password Manager")
window.config(pady=50, padx=50)  # Add padding around the window

# Logo setup
canvas = ttk.Canvas(window, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")  # Load logo image (make sure logo.png exists in directory)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# ---------------------------- LABELS ------------------------------- #
website_label = ttk.Label(window, text="Website:", font=Font)
website_label.grid(column=0, row=1, sticky="w")

email_label = ttk.Label(window, text="Email/Username:", font=Font)
email_label.grid(column=0, row=2, sticky="w")

password_label = ttk.Label(window, text="Password:", font=Font)
password_label.grid(column=0, row=3, sticky="w")

# ---------------------------- ENTRY FIELDS ------------------------------- #
website_entry = ttk.Entry(window, width=36)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()  # Focus cursor on website entry

email_entry = ttk.Entry(window, width=36)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "imuniqueshiv@gmail.com")  # Default email

password_entry = ttk.Entry(window, width=17)
password_entry.grid(column=1, row=3, sticky="w")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Lists of possible characters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['*', '!', '$', '#', '@', '&', '%', '?']


    print("Welcome to the PyPassword Generator!")  # Debug print (optional)

    # List to store password characters
    letters_add = [choice(letters) for _ in range(randint(8,10))]  # 8-10 random letters
    num_add = [choice(numbers) for _ in range(randint(2,4))]       # 2-4 numbers
    symbols_add = [choice(symbols) for _ in range(randint(2,4))]   # 2-4 symbols

    password_list = letters_add + symbols_add + num_add
    shuffle(password_list)  # Shuffle for randomness

    final_password = "".join(password_list)  # Convert to string
    password_entry.insert(0, final_password)  # Insert into entry box
    pyperclip.copy(final_password)  # Copy to clipboard

# ---------------------------- SAVE FUNCTION ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Validate inputs
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="⚠️ Error", message="Please make sure you haven't left any fields empty.")
        return

    # Ask for confirmation before saving
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                          f"Email: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        with open("data.txt", "r") as file:  # This block prints all entries — could get long over time
            print(file.read())

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- BUTTONS ------------------------------- #
generate_password_button = ttk.Button(window, text="Generate Password",
                                      command=password_generator, width=16, bootstyle="primary")
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = ttk.Button(window, text="Add", command=save_data, width=35, bootstyle="success")
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

# Run the application
window.mainloop()
