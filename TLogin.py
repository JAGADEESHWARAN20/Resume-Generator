from tkinter import * #type: ignore
from ttkbootstrap import Style
from tkinter import ttk,messagebox
from ttkbootstrap import * #type: ignore
from pymongo import MongoClient
import subprocess
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

Labelname = ttk.Label(text='Teacher Login',font=('helvetica rounded',18) )
Labelname.pack(side='top',pady=20)

# Create label frame
login_frame = ttk.LabelFrame(window, text="Login")
login_frame.pack(side=TOP,pady=80 ,ipadx=50,ipady=30,anchor=CENTER)

username = ttk.Label(login_frame,text='Username')
username.pack(side='top',padx=5,pady=15,anchor=CENTER)
user_entry = ttk.Entry(login_frame)
user_entry.pack(side='top',padx=10,pady=15,anchor=CENTER)

password = ttk.Label(login_frame,text='Password')
password.pack(side='top',padx=5,pady=5,anchor=CENTER)
password_entry = ttk.Entry(login_frame,show='*')
password_entry.pack(side='top',padx=10,pady=10,anchor=CENTER)

def login(username, password):
    try:
        # connect to the database
        client = MongoClient('mongodb://localhost:27017')
        db = client['StudentDatabase']
        collection = db['StudentLogin']
        
        # query the collection for the user
        user = collection.find_one({'username': username})
        
        if user and user['password'] == password:
            # show a success message if the user was found and the password is correct
            messagebox.showinfo('Login', 'Login successful!')
            subprocess.Popen('')
            
        else:
            # show an error message if the user was not found or the password is incorrect
            messagebox.showerror('Login', 'Invalid username or password.')
    except:
        # show an error message if the connection failed
        messagebox.showerror('Login', 'Could not connect to the database.')
      



login_button = ttk.Button(login_frame, text='Login',command=lambda: login(user_entry.get(), password_entry.get()))
login_button.pack(side='bottom', pady=10)

registration = ttk.Button(window,text='Register')
registration.pack(side='bottom',pady=15)

def exit_window():
  window.destroy()

Xit = ttk.Button(window,bootstyle='danger',text='x',command=exit_window) # type: ignore 
Xit.place(x=370,y=0)

# Run the window
window.mainloop()
