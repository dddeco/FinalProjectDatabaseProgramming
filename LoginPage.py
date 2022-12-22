import os
from tkinter import *
import pandas as pd
from tkinter import Image
from PIL import ImageTk
from PIL import Image
import tkinter.messagebox
from SQLServerWriteIn import WriteIn
from MainPage import *

class LoginPage:
    def __init__(self,master):
        self.root=master
        self.root.title('Insurance System Login')
        self.create()

    def create(self):
        image2 = Image.open('cloud.png')
        background_image = ImageTk.PhotoImage(image2)
        w = background_image.width()
        h = background_image.height()
        self.root.geometry('%dx%d+200+100' % (w, h))
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        tk.Label(root, text='User:').place(x=420, y=250)
        tk.Label(root, text='Password:').place(x=420, y=290)
        self.var_usr_name = tk.StringVar()
        entry_usr_name = tk.Entry(root, textvariable=self.var_usr_name)
        entry_usr_name.place(x=480, y=250)
        self.var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(root, textvariable=self.var_usr_pwd, show='*')
        entry_usr_pwd.place(x=480, y=290)

        bt_login = tk.Button(root, text='Login', command=self.usr_log_in)
        bt_login.place(x=440, y=330)
        bt_logup = tk.Button(root, text='Register', command=self.usr_sign_up)
        bt_logup.place(x=510, y=330)
        bt_logquit = tk.Button(root, text='Exit', command=self.usr_sign_quit)
        bt_logquit.place(x=590, y=330)

        mainloop()

    def usr_log_in(self):
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        flag = 0
        if os.path.exists('EmployeeUpdate.csv'):
            df = pd.read_csv('EmployeeUpdate.csv')
            array = df.values
            for i in range(len(array)):
                if array[i][1] == usr_name:
                    # array[i][2] = array[i][2].rstrip()
                    if array[i][2] == usr_pwd:
                        flag = 1

        df2 = pd.read_csv('Employee.csv')
        array2 = df2.values
        for i in range(len(array2)):
            if array2[i][1] == usr_name:
                array2[i][2] = array2[i][2].rstrip()
                if array2[i][2] == usr_pwd :
                    flag = 1

        if (flag == 1):
            tk.messagebox.showinfo(title='welcome',
                                   message='Welcome：' + usr_name)
            if os.path.exists('EmployeeUpdate.csv'):
                try:
                    os.remove('EmployeeUpdate.csv')
                except BaseException as e:
                    print(e)
            MainPage()
            self.root.destroy()
        elif(flag == 0):
            tk.messagebox.showinfo(message='Please enter right Username and Password.')
                #MainPage()

    def usr_sign_up(self):
        def signtowcg():
            nn = new_name.get()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            df = pd.read_csv('Employee.csv')
            array = df.values
            for i in range(len(array)):
                if array[i][1] == nn + ' ':
                    tk.messagebox.showerror('Error', 'Username already exists')
                elif np == '' or nn == '':
                    tk.messagebox.showerror('Error', 'Username and password cannot be blank')
                elif np != npf:
                    tk.messagebox.showerror('Error', 'The password you entered does not match.Please reenter the password.')
                else:
                     num = int(df.iloc[-1][0] + 1)
                     data = {"EmployeeID": [num],
                             "EmployeeAcctName": [nn],
                             "EmployeetPswd": [np]}
                     new_df = pd.DataFrame(data)
                     #df2 = pd.DataFrame(numpy.insert(df.values, len(df.index), values=[num, nn, np], axis=0))
                     #df2.columns = df.columns
                     #df2 = df.merge(df, new_df)
                     new_df.to_csv('EmployeeUpdate.csv',encoding='utf-8',index=False)
                     WriteIn('EmployeeUpdate.csv')
                     tk.messagebox.showinfo('Welcome', 'Registration Complete.')
                     root_sign_up.destroy()
                     break



        root_sign_up = tk.Toplevel(root)
        root_sign_up.geometry('350x200')
        root_sign_up.title('Register')
        new_name = tk.StringVar()
        tk.Label(root_sign_up, text='Username：').place(x=70, y=10)
        tk.Entry(root_sign_up, textvariable=new_name).place(x=150, y=10)
        new_pwd = tk.StringVar()
        tk.Label(root_sign_up, text='Password：').place(x=70, y=50)
        tk.Entry(root_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
        new_pwd_confirm = tk.StringVar()
        tk.Label(root_sign_up, text='Re-enter password：').place(x=30, y=90)
        tk.Entry(root_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
        bt_confirm_sign_up = tk.Button(root_sign_up, text='Register Comfirmation',
                                       command=signtowcg)
        bt_confirm_sign_up.place(x=150, y=130)



    def usr_sign_quit(self):
        root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)
