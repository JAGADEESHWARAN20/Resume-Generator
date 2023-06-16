from tkinter import * #type: ignore
from ttkbootstrap import Style
from tkinter import ttk,messagebox
import subprocess
from ttkbootstrap import * #type: ignore
from pymongo import MongoClient
import re

# Create window
window = Tk()
window.title("Teacher Login")
window.geometry("400x600")

# Create style object
style = Style(theme='vapor')
width_of_window = 400
height_of_window = 600
window.resizable(False, False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)

window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

window.overrideredirect(True)

Labelname = ttk.Label(text='Teacher Registration',font=('helvetica rounded',18) )
Labelname.pack(side='top',pady=40)

# Create label frame
Registration_frame = ttk.LabelFrame(window, text="Login")
Registration_frame.pack(side=TOP,ipadx=50,anchor=CENTER)

FullName = ttk.Label(Registration_frame,text='Full Name')
FullName.pack(side='top',padx=5,pady=5)
FullName_entry = ttk.Entry(Registration_frame)
FullName_entry.pack(side='top',padx=10,pady=10,fill=X)

Email = ttk.Label(Registration_frame,text='Email')
Email.pack(side='top',padx=5,pady=5)
Email_entry = ttk.Entry(Registration_frame)
Email_entry.pack(side='top',padx=10,pady=10,fill=X)

Username = ttk.Label(Registration_frame,text='Username')
Username.pack(side='top',padx=5,pady=5)
Username_entry = ttk.Entry(Registration_frame)
Username_entry.pack(side='top',padx=10,pady=10,fill=X)

password = ttk.Label(Registration_frame,text='Password')
password.pack(side='top',padx=5,pady=5)
password_entry = ttk.Entry(Registration_frame,show='*')
password_entry.pack(side='top',padx=10,pady=10,fill=X)




def validate_input():
    # define regex patterns for email, username, and password
    email_pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    username_pattern = fr'^[a-zA-Z0-9_]+$'
    password_pattern = r'^[a-zA-Z0-9@#$%^&+=]{8,}$'

    # validate email field
    if not re.match(email_pattern, Email_entry.get()):
        # handle invalid email address
        messagebox.showerror('Invalid','Invalid email address')
        return False

    # validate username field
    if not re.match(username_pattern, Username_entry.get()):
        # handle invalid username
        messagebox.showerror('Invalid Username','Username should contain only letters, digits and underscores')
        return False

    # validate password field
    if not re.match(password_pattern, password_entry.get()):
        # handle invalid password
        messagebox.showerror('Invalid Password','Password should be at least 8 characters long and contain letters, digits, and special characters')
        return False

    # all fields are valid
    return True

def register(full_name,email,username,password):
  try:
    # check if all fields are valid
    if not validate_input():
        return

    # connect to the database
    client = MongoClient('mongodb://localhost:27017')
    db = client['StudentDatabase']
    collection = db['StudentLogin']

    # check if username already exists in the database
    if collection.find_one({'username': Username_entry.get()}):
        messagebox.showerror('Registration', 'Username already exists. Please choose a different username.')
        return

    # insert a new user document into the collection
    new_user = {
        'full_name': FullName_entry.get(),
        'email': Email_entry.get(),
        'username': Username_entry.get(),
        'password': password_entry.get()
    }
    collection.insert_one(new_user)

    # show a success message if the insertion was successful
    messagebox.showinfo('Registration', 'Registration successful!')
    def loginopen():
      window.destroy()
      subprocess.Popen('login.exe')
    window.after(1000,loginopen)
  except:
        # show an error message if the connection failed or the insertion failed
    messagebox.showerror('Registration', 'Could not register user.')



registration = ttk.Button(Registration_frame,text='Register',command=lambda: register(
    full_name=FullName_entry.get(),
    email=Email_entry.get(),
    username=Username_entry.get(),
    password=password_entry.get()
))
registration.pack(side='bottom',pady=15)


login_button = ttk.Button(window, text='Login')
login_button.pack(side='bottom', pady=10)

def exit_window():
  window.destroy()

Xit = ttk.Button(window,bootstyle='danger',text='x',command=exit_window) # type: ignore 
Xit.place(x=370,y=0)

# Run the window
window.mainloop()