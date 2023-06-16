"""from ttkbootstrap import Style, Label, Progressbar
import subprocess
from tkinter import * #type:ignore
import tkinter as tk

root = Tk()
root.geometry("600x400")

Style(theme='vapor')

width_of_window = 600
height_of_window = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))






root.mainloop()

"""




import tkinter as tk
from tkinter import ttk

class LoadingScreen(tk.Toplevel):
    def __init__(self, parent, main_label_text='', sub_label_text='', footer_text=''):
        super().__init__(parent)
        self.title('Loading...')
        self.geometry('400x200')
        self.resizable(False, False)

        main_label = ttk.Label(self, text=main_label_text, font=('Arial', 16))
        main_label.pack(pady=10)

        sub_label = ttk.Label(self, text=sub_label_text, font=('Arial', 12))
        sub_label.pack()

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=200, mode='indeterminate')
        self.progress_bar.pack(pady=10)

        footer_label = ttk.Label(self, text=footer_text, font=('Arial', 8))
        footer_label.pack(side='bottom', pady=10)

    def start(self):
        self.progress_bar.start()

    def stop(self):
        self.progress_bar.stop()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    loading_screen = LoadingScreen(root, main_label_text='Loading', sub_label_text='Please wait...', footer_text='Powered by Tkinter')
    loading_screen.start()
    # do some work here
    loading_screen.stop()
    loading_screen.destroy()
    root.destroy()
