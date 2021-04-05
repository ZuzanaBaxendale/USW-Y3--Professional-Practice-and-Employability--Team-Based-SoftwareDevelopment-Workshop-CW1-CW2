from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Accept Policy Before Continuing")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 500
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def open_policy():
    window = Toplevel(root)
    policytext = Text(window, height =20, width=30)
    policytext.pack()
    policytext.insert(END, "Data Protection Act (GDPA), induction and image usage\n")
    policytext.insert(END, "Definition of UK Law: \n")
    policytext.insert(END, "The Data Protection Act controls how your personal information is used by organisations,\n")
    policytext.insert(END, "businesses or the government, makes provision for a direct marketing code of practise and\n")
    policytext.insert(END, "also helps with connection purposes.\n")
    policytext.insert(END, "\n")

    accept = Button(window, text="ACCEPT")
    accept.pack()
    decline = Button(window, text="DECLINE")
    decline.pack()

b = Button(root, text="Policy", command=open_policy)
b.pack()

mainloop()