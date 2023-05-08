from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter= [choice(letters) for _ in range(randint(5, 8))]
    password_symbol=[choice(symbols) for _ in range(randint(2,4))]
    password_number=[choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letter+ password_symbol+ password_number
    shuffle(password_list)

    password="".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website= website_entry.get()
    email=email_username_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="Error", message="please don't leave entry blank")
    else:
        # creating a message box
        is_ok=messagebox.askokcancel(title= website, message=f"Details entered :\n Email: {email}\n Password: {password}\n Are you want to save ?")
        if is_ok== True:
            # create a text file
            with open("data.txt", "a") as data_file:
                # saving data  in data.txt file

                data_file.write(f"{website} | {email} |{password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            messagebox.showinfo(title="Password Manager", message="Password is not Saved")

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
# screen
window.title("Password Manager")
window.minsize(width= 500, height= 400)
window.config(padx=20 , pady=20)


#canvas is created to place image in screen
canvas=Canvas(width= 200, height=200)
# image name= LOCK_IMG
lock_img= PhotoImage(file="logo.png")
# image is created
canvas.create_image(100, 96, image=lock_img)
canvas.grid(row=0 , column=1)

# labels creating
# website label
website_label=Label(text="Website:")
website_label.grid(row=1 , column=0)
# Email/Username label
email_username_label=Label(text="Email/Username:")
email_username_label.grid(row=2 , column=0)
# Password label
password_label= Label(text="Password :    ")
password_label.grid(row=3 , column=0 )

# Entry creating
# website Entry
website_entry=Entry(width= 35)
website_entry.grid(row=1, column=1, columnspan=2)
# cursor in the entry by focus()
website_entry.focus()
# Email/Username Entry
email_username_entry=Entry(width= 35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0,"albinreji56@gmail.com")
# Password entry
password_entry=Entry(width=21)
password_entry.place(x= 95,y=246)

# Click button is creating
# Add button
add_button=Button(width= 30, text="Add", command=save)
add_button.place(x=100, y=280)
# generate_password button
generate_password_button= Button(text="Genreate Password", command=generate_password)
generate_password_button.place( x= 205,y=245)


window.mainloop()