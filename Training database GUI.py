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
        "CREATE TABLE IF NOT EXISTS `TrainingCourses` (empNo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, salary TEXT, taxcode TEXT, nationalinsurance TEXT)")


def Create():
    if EmpNo.get() == "" or CourseCode.get() == "" or CourseName.get() == "" or CourseAvailable.get() == "" or CourseTaken.get() == "" or CourseDate.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `TrainingCourses` (ApplicantForename, ApplicantSurname, JobAppliedFor, DateOfEMTest, MathsScore, EnglishScore) VALUES(?, ?, ?, ?, ?, ?)",
                       (str(EmpNo.get()), str(CourseCode.get()), str(CourseName.get()), bool(CourseAvailable.get()), bool(CourseTaken.get()), str(CourseTaken.get())))
        conn.commit();
        EmpNo.set("");
        CourseCode.set("");
        CourseName.set("");
        CourseTaken.set(False);
        CourseAvailable.set(False);
        CourseDate.set("");

        cursor.close();
        conn.close();
        txt_result.config(text="TrainingCourse Record is Created!", fg="green")


def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `TrainingCourses`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the records from Applicants", fg="green")


def Exit():
    result = tkMessageBox.askquestion('Training', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


EmpNo = StringVar()
CourseCode = StringVar()
CourseName = StringVar()
CourseDate = StringVar()
CourseTaken = bool()
CourseAvailable = bool()


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



txt_title = Label(Top, width=900, font=('arial', 24), text="Training")
txt_title.pack()

txt_EmpNo = Label(Forms, text="Employee number:", font=('arial', 10), bd=15)
txt_EmpNo.grid(row=0, stick="e")
txt_CourseCode = Label(Forms, text="Course code:", font=('arial', 10), bd=15)
txt_CourseCode.grid(row=1, stick="e")
txt_CourseName = Label(Forms, text="Course Name:", font=('arial', 10), bd=15)
txt_CourseName.grid(row=2, stick="e")
txt_CourseTaken = Label(Forms, text="Is the course being taken?:", font=('arial', 10), bd=15)
txt_CourseTaken .grid(row=3, stick="e")
txt_CourseAvailable = Label(Forms, text="Do you think the course will be available?:", font=('arial', 10), bd=15)
txt_CourseAvailable.grid(row=4, stick="e")
txt_CourseDate = Label(Forms, text="Date of Course:", font=('arial', 10), bd=15)
txt_CourseDate.grid(row=5, stick="e")

txt_result = Label(Buttons)
txt_result.pack(side=TOP)

EmpNo = Entry(Forms, textvariable=EmpNo, width=30)
EmpNo.grid(row=0, column=1)
CourseCode = Entry(Forms, textvariable=CourseCode, width=30)
CourseCode.grid(row=1, column=1)
CourseName = Entry(Forms, textvariable=CourseName, width=30)
CourseName.grid(row=2, column=1)
CourseTaken = Entry(Forms, textvariable=CourseTaken, width=30)
CourseTaken.grid(row=3, column=1)
CourseAvailable = Entry(Forms, textvariable=CourseAvailable, width=30)
CourseAvailable.grid(row=4, column=1)
CourseDate = Entry(Forms, textvariable=CourseDate, width=30)
CourseDate.grid(row=5, column=1)


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
tree = ttk.Treeview(Right, columns=("EmpNo", "CourseCode", "CourseName", "CourseTaken", "CourseAvailable", "CourseDate"), selectmode= "extended", height=500,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview);
scrollbary.pack(side=RIGHT, fill=Y);
scrollbarx.config(command=tree.xview);
scrollbarx.pack(side=BOTTOM, fill=X);
tree.heading('EmpNo', text="Employee number", anchor=W);
tree.heading('CourseCode', text="Course Code", anchor=W);
tree.heading('CourseName', text="Course Name", anchor=W);
tree.heading('CourseTaken', text="Course Taken", anchor=W);
tree.heading('CourseAvailable', text="Course Available", anchor=W);
tree.heading('CourseDate', text ="Date of course", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)


tree.pack()

if __name__ == '__main__':
    root.mainloop()