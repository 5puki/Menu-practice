from tkinter import *
from tkinter import filedialog

def savethis():
    file = filedialog.asksaveasfile(initialdir = "C:\\Users\\Spuki\\PycharmProjects\\pythonProject\\venv",
                                    defaultextension=".txt",
                                    filetypes = [
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])

def newtext():
    print("You have opened a new file!")

def undo():
    print("You undid the last action!")

def about():
    print("I will make menus!")

window = Tk()

themenubar = Menu(window)
window.config(menu = themenubar)

filesmenu = Menu(themenubar, tearoff = 0)
themenubar.add_cascade(label = "File", menu = filesmenu)
filesmenu.add_command(label = "New", command = newtext)
filesmenu.add_command(label = "Save", command = savethis)
filesmenu.add_separator()
filesmenu.add_command(label = "Exit", command = quit)

editmenu = Menu(themenubar, tearoff = 0)
themenubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Undo", command = undo)

aboutmenu = Menu(themenubar, tearoff = 0)
themenubar.add_cascade(label = "About", menu = aboutmenu)
aboutmenu.add_command(label = "What is this?", command = about)

window.mainloop()