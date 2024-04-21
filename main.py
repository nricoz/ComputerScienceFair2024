from tkinter import *
import os

root = Tk()
root.title("Teacher's Portal - Login")
root.geometry("400x400")

class Teacher:
    def __init__(self, teacher):
        self.teacher = teacher

def run(teacher):
    #Writes teacher name to file so that program can look to detect right face
    # printf %s removes newline, so that it doesn't cause FileNotFoundError: [Errno 2] No such file or directory: '/Users/user/Downloads/ComputerScienceFair Project/images/demosthenes\n/image1.png'
    os.system(f'printf %s "{teacher}" > teacher.txt')
    root.destroy()
    os.system("python3 login.py")

demosthenes = Button(root, text="Nora Demosthenes", command=lambda:run("demosthenes"))
rivero = Button(root, text="Jeffrey Rivero", command=lambda:run("rivero"))

demosthenes.pack()
rivero.pack()

root.mainloop()