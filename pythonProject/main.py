from tkinter import *
import mysql.connector
from PIL import ImageTk
from singup import login_singup
from tkinter import messagebox
from lobby import lobby
class Hello:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x600+40+50')
        self.root.title("User Login")
        self.root.resizable('false', 'false')




# =================================== first frame ================================================
        self.fram_side = Frame(self.root, width=350, height=900, bg="#00FFFF")
        self.fram_side.place(x=0, y=0)
# ===================================== second frame =============================================
        self.sub_left_fram = Frame(self.root, width=200, height=500, relief=RAISED, bd=1, bg="#00FFFF")
        self.sub_left_fram.place(x=150, y=50)

        # ****************************** heading *******************************
        self.pic = ImageTk.PhotoImage(file="logo3.png")
        self.pic_lbl = Label(self.sub_left_fram, image=self.pic, bd=0, bg="#00FFFF")
        self.pic_lbl.place(x=0, y=0)
# ====================================== third frame ====================================
        self.main_frame = Frame(self.root, width=800, height=500, relief=RAISED, bd=1, bg="white")
        self.main_frame.place(x=350, y=50)

        # ************************************* picture ***********************************
        self.login_logo_pic = ImageTk.PhotoImage(file="login4.jfif")
        self.login_lbl = Label(self.main_frame, image=self.login_logo_pic, borderwidth=0)
        self.login_lbl.place(x=270, y=20)

        # *********************************** labels ***************************************
        self.lbl_username = Label(self.main_frame, text="User Name", font=('times new roman', 15, 'bold'), bg="white")
        self.lbl_username.place(x=300, y=250)

        self.lbl_password = Label(self.main_frame, text="Password",  font=('times new roman', 15, 'bold'), bg="white")
        self.lbl_password.place(x=300, y=320)


        # *********************************** entries **************************************
        user_name = StringVar()
        password = StringVar()
        self.txt_username = Entry(self.main_frame, font=(12), border=2)
        self.txt_username.place(x=300, y=280)
        self.txt_username = Entry(self.main_frame, font=(12), border=2)
        self.txt_username.place(x=300, y=360)

        # ************************************** functions **************************************


        def remove():
            pass


        def submit():
            coon = mysql.connector.connect(host="localhost", user="root", database="second_sem")
            my_cursor = coon.cursor()
            my_cursor.execute("Select * from try_data where email = %s and user_password = %s", (
                user_name.get(),
                password.get()))
            row = my_cursor.fetchone()
            if row == None or row == "":
                messagebox.showerror("error", "email or password wrong")
            else:
                messagebox.showinfo('info', 'fetching successfully')
            coon.commit()
            coon.close()

        def fun_singup():
            variable_singup = Toplevel(self.root)
            singup_page = login_singup(variable_singup)




        # ************************************** btn *******************************************

        self.btn_img = ImageTk.PhotoImage(file="singh6.png")
        self.btn_sing = Button(self.main_frame, command=submit, image=self.btn_img, bd=0, bg="white")
        self.btn_sing.place(x=150, y=404)

        self.pic2 = ImageTk.PhotoImage(file="singimgae.png")
        self.btn_sing = Button(self.main_frame, command=fun_singup, text="Sing Up", compound="left", image=self.pic2, bd=0, bg="white", font=('times new roman', 25, 'bold'))
        self.btn_sing.place(x=550, y=5)

        self.btn_reset = Button(self.main_frame, command=remove, text="Remove", bd=0, bg="white", fg="red")
        self.btn_reset.place(x=450, y=390)


if __name__ == '__main__':
    root = Tk()
    obj = Hello(root)
    root.mainloop()

    '''record = mysql.connector.connect(host="localhost", username="root", database="second_sem")
    my_cursor = record.cursor()
    my_cursor.execute("select * from singup_table where email = %s;")
    try_fetch = my_cursor.fetchone()
    user_fetch = try_fetch[0]
    # pass_fetch = try_fetch[0]
    if user_fetch != 0:
        pass_query = "SELECT user_password from singup_table Where email = %s"
        my_cursor.execute(pass_query, (username.get()))
        tuple_valid_pass = my_cursor.fetchone()
        password_validation = tuple_valid_pass[0]

        if password_validation == password.get():
            messagebox.showinfo("info", "mission successful")
        else:
            messagebox.showerror("error", "something went wrong")
    else:
        messagebox.showerror('error', "not exist")'''


    '''query = ("select * from first_sing_up where email=%s")
            value = (email.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("error", "this email is exist")
            else:'''