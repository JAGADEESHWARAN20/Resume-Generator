
import tkinter as tk
from tkinter import * #type:ignore
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from ttkbootstrap import Style


root = Tk()
root.title("Teacher")

style = Style(theme='vapor')

# Set window size and position
width_of_window = 800
height_of_window = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

# Create a frame for the NavBar and set its style
nav_bar_frame = ttk.Frame(root)
nav_bar_frame.pack(side="left", fill="y")

# Create a Labelframe for the NavBar
nav_bar = ttk.LabelFrame(nav_bar_frame, text='NavMenu', width=200, height=800)
nav_bar.pack(side='top', padx=10, pady=10, fill='both', expand=True)

notification_bar = ttk.LabelFrame(nav_bar_frame, text='Notification', width=200, height=300)
notification_bar.pack(side='top', padx=10, pady=10, fill='both', expand=True)




# Create a button for the Academics and add it to the NavMenu
academics_button = ttk.Button(nav_bar, text='Academics', command=lambda: print("Academics clicked"))
academics_button.pack(side='top', pady=10, padx=10, fill='x')

# Create a frame for the Student Details and set its style
student_details_frame = ttk.Frame(root)
student_details_frame.pack(side="left", fill="both", expand=True)

# Create a Labelframe for the Student Details
student_details = ttk.LabelFrame(student_details_frame, text='Teacher Main Screen', width=600, height=800)
student_details.pack(side='top', padx=10, pady=10, fill='both', expand=True)

# Create a button for going back to the previous screen and add it to the student details frame
back_button = ttk.Button(student_details, text='BACK', command=root.quit)
back_button.pack(side='bottom', pady=10, padx=10, anchor='e')

# Create a search bar for searching students and add it to the student details frame
search_label = ttk.Label(student_details, text='Search Student:')
search_label.pack(side=TOP, padx=10, pady=10)




def student_list():
    student_details.config(text='Student List')
    
    student_list_label = ttk.Label(student_details,text='Student List',font=('poppins medium',18) )
    student_list_label.pack(side=TOP,anchor='center')
    def search_students():  
        
        search_query = search_entry.get().lower()
        # Connect to the database
        conn = sqlite3.connect('personal.db')
        # Create a cursor
        c = conn.cursor()
        if search_query == '':
            # If search_query is empty, fetch all student details from the database
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        else:
            # Fetch the student details that match the search query
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        students = c.fetchall()
        # Close the database connection
        conn.close()

        table.delete(*table.get_children())

        if not students:
            # If no student details are found, show a message in the table
            table.insert('', 'end', values=('No matching records found',), tags=('button'))
            
            Nodata = ttk.Label(student_details,text='No Records in Database',bootstyle='info')#type:ignore
            Nodata.place(y=700,x=200)
            
            
            if search_entry == '' and not students:
                Nodata = ttk.Label(student_details,text='No Records in Database',bootstyle='info')#type:ignore
                Nodata.place(y=700,x=200)
                Nodata.destroy()
                
        # If search_query is empty and no student details are found, remove the Nodata label
                
        else:
            for student in students:
                table.insert('', 'end', values=(student[0], student[1], student[2], student[3]), tags=('button'))
            table.tag_configure('button', font=('Arial', 8))

        if search_query == '':
            # If search_query is empty, wait for 1 second and then show all student details
            root.after(1000, lambda: search_students())
            
    search_entry = ttk.Entry(student_details, width=30)
    search_entry.pack(side=TOP, padx=10, pady=10,anchor='e')

    search_button = ttk.Button(student_details, text='Search',command=search_students)
    search_button.pack(side=TOP , padx=5, pady=5,anchor='e')
    
    # Connect to the database
    conn = sqlite3.connect('Updater.db')
    # Create a cursor
    c = conn.cursor()
    # Fetch all the student details from the database
    c.execute("SELECT * FROM Resume")
    students = c.fetchall()
    # Close the database connection
    for student in students:
        print(student)
    
    conn.close()

    table = ttk.Treeview(student_details, columns=('col1', 'col2', 'col3', 'col4'), show='headings')
    table.pack(anchor='center',fill='both',expand=TRUE,padx=5)

    table.column('col1', width=120, anchor='center')
    table.heading('col1', text='Name', anchor='center')  # type: ignore
    table.column('col2', width=100, anchor='center')
    table.heading('col2', text='Contact', anchor='center')
    table.column('col3', width=200, anchor='center')
    table.heading('col3', text='Address', anchor='center')
    table.column('col4', width=100, anchor='center')
    table.heading('col4', text='DOB', anchor='center')
    
    style = ttk.Style()
    style.configure("Treeview.Heading", background="#673AB7",foreground='white')
        
    
    for student in students:
        table.insert('', 'end', values=(student[0], student[1], student[2],student[3]), tags=('button'))

    table.tag_configure('button', font=('Arial', 8))
    
    





Main_screen = ttk.Button(nav_bar, text='Main Screen',command=student_list)
Main_screen.pack(side='top', padx=10, pady=10, fill='x')


root.mainloop()


