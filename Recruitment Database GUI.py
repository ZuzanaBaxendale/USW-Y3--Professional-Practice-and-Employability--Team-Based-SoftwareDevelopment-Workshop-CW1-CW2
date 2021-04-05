from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Recruitment")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1500
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



def Database():
    global conn, cursor
    conn = sqlite3.connect('ufixRT.s3db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `Applicants` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, salary TEXT, taxcode TEXT, nationalinsurance TEXT)")


def Create():
    if ApplicantForename.get() == "" or ApplicantSurname.get() == "" or JobAppliedFor.get() == "" or DateOfEMTest.get() == "" or MathsScore.get() == "" or EnglishScore.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `Applicants` (ApplicantForename, ApplicantSurname, JobAppliedFor, DateOfEMTest, MathsScore, EnglishScore) VALUES(?, ?, ?, ?, ?, ?)",
                       (str(ApplicantForename.get()), str(ApplicantSurname.get()), str (JobAppliedFor.get()), str (DateOfEMTest.get()), int (MathsScore.get()), int (EnglishScore.get())))
        conn.commit();
        ApplicantForename.set("");
        ApplicantSurname.set("");
        JobAppliedFor.set("");
        DateOfEMTest.set("");
        MathsScore.set("");
        EnglishScore.set("");

        cursor.close();
        conn.close();
        txt_result.config(text="Applicant Record is Created!", fg="green")


def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `Applicants`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the records from Applicants", fg="green")


def Exit():
    result = tkMessageBox.askquestion('Recruitment', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


ApplicantForename = StringVar()
ApplicantSurname = StringVar()
JobAppliedFor = StringVar()
DateOfEMTest = StringVar()
MathsScore = IntVar()
EnglishScore = IntVar()


Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)



txt_title = Label(Top, width=900, font=('arial', 24), text="Recruitment")
txt_title.pack()

txt_Forename = Label(Forms, text="Forename:", font=('arial', 10), bd=15)
txt_Forename.grid(row=0, stick="e")
txt_Surname = Label(Forms, text="Surname:", font=('arial', 10), bd=15)
txt_Surname.grid(row=1, stick="e")
txt_JobAppliedFor = Label(Forms, text="Job Applied For:", font=('arial', 10), bd=15)
txt_JobAppliedFor.grid(row=2, stick="e")
txt_DateOfEMTest = Label(Forms, text="Date of English and Maths Test:", font=('arial', 10), bd=15)
txt_DateOfEMTest.grid(row=3, stick="e")
txt_EnglishResult = Label(Forms, text="English Result:", font=('arial', 10), bd=15)
txt_EnglishResult.grid(row=4, stick="e")
txt_MathsResult = Label(Forms, text="Maths Result:", font=('arial', 10), bd=15)
txt_MathsResult.grid(row=5, stick="e")

txt_result = Label(Buttons)
txt_result.pack(side=TOP)

ApplicantForename = Entry(Forms, textvariable=ApplicantForename, width=30)
ApplicantForename.grid(row=0, column=1)
ApplicantSurname = Entry(Forms, textvariable=ApplicantSurname, width=30)
ApplicantSurname.grid(row=1, column=1)
JobAppliedFor = Entry(Forms, textvariable=JobAppliedFor, width=30)
JobAppliedFor.grid(row=2, column=1)
DateOfEMTest = Entry(Forms, textvariable=DateOfEMTest, width=30)
DateOfEMTest.grid(row=3, column=1)
MathsScore = Entry(Forms, textvariable=MathsScore, width=30)
MathsScore.grid(row=4, column=1)
EnglishScore = Entry(Forms, textvariable=EnglishScore, width=30)
EnglishScore.grid(row=5, column=1)


btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)


scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("ApplicantForename", "ApplicantSurname", "JobAppliedFor", "DateOfEMTest", "MathsScore", "EnglishScore"), selectmode= "extended", height=500,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview);
scrollbary.pack(side=RIGHT, fill=Y);
scrollbarx.config(command=tree.xview);
scrollbarx.pack(side=BOTTOM, fill=X);
tree.heading('ApplicantForename', text="Applicant Forename", anchor=W);
tree.heading('ApplicantSurname', text="Applicant Surname", anchor=W);
tree.heading('JobAppliedFor', text="Job Applied For", anchor=W);
tree.heading('DateOfEMTest', text="Date of Maths and English Test", anchor=W);
tree.heading('MathsScore', text="Maths Score", anchor=W);
tree.heading('EnglishScore', text="English Score", anchor=W);
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)

tree.pack()

if __name__ == '__main__':
    root.mainloop()