from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk

class login_singup:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x650+40+30')
        self.root.title("User Login")
        self.root.resizable('false', 'false')

        # =================================== first frame ================================================
        self.fram_side = Frame(self.root, width=350, height=900, bg="#00FFFF")
        self.fram_side.place(x=0, y=0)
        # ===================================== second frame =============================================
        self.sub_left_fram = Frame(self.root, width=200, height=500, relief=RAISED, bd=1, bg="#00FFFF")
        self.sub_left_fram.place(x=150, y=50)

        self.lbl_heading = Label(self.sub_left_fram, text="Sing Up", font=('Times new roman', 20, 'bold'), bg="#00FFFF")
        self.lbl_heading.place(x=0, y=0)

        self.pic = ImageTk.PhotoImage(file="school_project_logo.png")
        self.pic_lbl = Label(self.sub_left_fram, image=self.pic, bd=0, bg="#00FFFF")
        self.pic_lbl.place(x=0, y=0)
        # ========== third frame ====================================
        self.main_frame = Frame(self.root, width=800, height=500, relief=RAISED, bd=1, bg="white")
        self.main_frame.place(x=350, y=50)

        self.lbl_heading_school = Label(self.main_frame, text="School Management System", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_heading_school.place(x=235, y=0)

        # **************************************** labels *******************************************
        self.lbl_fn = Label(self.main_frame, text="First Name", bg="white", font=('arial', 12, 'bold'))
        self.lbl_fn.place(x=200, y=60)
        self.lbl_ln = Label(self.main_frame, text="Last Name", bg="white", font=('arial', 12, 'bold'))
        self.lbl_ln.place(x=200, y=110)
        self.lbl_email = Label(self.main_frame, text="Email", bg="white", font=('arial', 12, 'bold'))
        self.lbl_email.place(x=200, y=160)
        self.lbl_password = Label(self.main_frame, text="Password", bg="white", font=('arial', 12, 'bold'))
        self.lbl_password.place(x=200, y=210)
        self.lbl_conf_password = Label(self.main_frame, text="Confirm Password", bg="white", font=('arial', 12, 'bold'))
        self.lbl_conf_password.place(x=200, y=260)
        self.lbl_gender = Label(self.main_frame, text="Gender", bg="white", font=('arial', 12, 'bold'))
        self.lbl_gender.place(x=200, y=310)
        self.lbl_phone = Label(self.main_frame, text="Phone No. ", bg="white", font=('arial', 12, 'bold'))
        self.lbl_phone.place(x=200, y=400)
        # **************************************** variables *************************************************
        v = tk.StringVar()
        first_name = StringVar()
        last_name = StringVar()
        email = StringVar()
        password = StringVar()
        phone = StringVar()
        # **************************************** entries ***************************************************
        self.txt_fn = Entry(self.main_frame, textvariable=first_name, bd=1, bg="silver", width=20, font=12, borderwidth=5)
        self.txt_fn.place(x=390, y=60)
        self.txt_fn.focus()
        self.txt_ln = Entry(self.main_frame, textvariable=last_name, bd=1, bg="silver", width=20, font=12, borderwidth=5)
        self.txt_ln.place(x=390, y=110)
        self.txt_ln.focus()

        self.txt_email = Entry(self.main_frame, bd=1, textvariable=email, bg="silver", width=20, font=12, borderwidth=5)
        self.txt_email.place(x=390, y=160)
        self.txt_email.focus()

        self.txt_password = Entry(self.main_frame, bd=1, textvariable=password, show="*", bg="silver", width=20, font=12, borderwidth=5)
        self.txt_password.place(x=390, y=210)
        self.txt_password.focus()

        self.txt_conf_password = Entry(self.main_frame, textvariable=password, show="*", bd=1, bg="silver", width=20, font=12, borderwidth=5)
        self.txt_conf_password.place(x=390, y=260)
        self.txt_conf_password.focus()

        self.txt_phone_no = Entry(self.main_frame, bd=1, textvariable=phone, bg="silver", width=20, font=12, borderwidth=5)
        self.txt_phone_no.place(x=390, y=400)

        # ************************************ gender ***************************************
        self.male = Radiobutton(self.main_frame, variable=v, value='male', text="Male")
        self.male.place(x=390, y=310)
        self.male.focus()

        self.female = Radiobutton(self.main_frame, variable=v, value='female', text="Female")
        self.female.place(x=390, y=340)
        self.female.focus()
        # ************************************* functions ***********************************
        def submit():
            record = mysql.connector.connect(host="localhost", username="root", database="second_sem")
            my_cursor = record.cursor()
            query = ("select * from try_data where email= %s")
            value = (email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("error", "this email is exist")
            else:
                my_cursor.execute("Insert into try_data values (%s, %s, %s, %s, %s, %s)", (first_name.get(),
                                                                                           last_name.get(),
                                                                                           email.get(),
                                                                                           password.get(),
                                                                                           phone.get(),
                                                                                           v.get()))
                messagebox.showinfo("info", "record successfully")
                record.commit()
                record.close()

        def clear():
            first_name.set("")
            last_name.set("")
            email.set("")
            password.set("")
            phone.set("")
            v.set("")

        # ************************************* buttons *****************************************
        self.btn_submit = Button(self.main_frame, text="Submit", command=submit, font=('times new roman', 20, 'bold'), width=10, height=1, bg="#00FFFF")
        self.btn_submit.place(x=65, y=443)

        self.btn_reset = Button(self.main_frame, command=clear, text="Clear", font=('times new roman', 20, 'bold'), width=12, height=1, bg="#00FFFF")
        self.btn_reset.place(x=270, y=443)

        self.btn_exit = Button(self.main_frame, text="Exit", command=exit, font=('times new roman', 20, 'bold'), width=12, height=1, bg="#00FFFF")
        self.btn_exit.place(x=500, y=443)



if __name__ == '__main__':
    root = Tk()
    obj = login_singup(root)
    root.mainloop()