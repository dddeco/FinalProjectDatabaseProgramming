import pandas as pd
import tkinter as tk
import pymongo
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='About System').pack()
        tk.Label(self,text='This system is a Product Recommendation System').pack()
        tk.Label(self, text='By typing in the ID of customers,').pack()
        tk.Label(self, text='This sytem would provide machine learning results to predict the probability of getting sick').pack()


class SearchFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        #.info_query = pd.DataFrame(columns={"pred_id","result"})
        self.id_Button = tk.Button(self,text='Search for predication data by ID',font=("Times",12),height=2,command=self.id_search)
        self.id_Button.pack()
        self.str1 = tk.StringVar()
        self.str2 = tk.StringVar()
        self.product = tk.StringVar()
        self.reslut = ""

    def closeit(self):
        self.label.pack_forget()
        self.pred_e.pack_forget()
        self.Button1.pack_forget()

    def showit(self,str1,str2,product):
        self.label1 = tk.Label(self,text='CustomerID: %s'%str1,font=("Times",12))
        self.label1.grid(row=1,column=1,padx=10,pady=10)
        self.label3 = tk.Label(self, text='Prediction: %s'%str2, font=("Times", 12))
        self.label3.grid(row=2, column=1, padx=10,pady=10)
        self.label5 = tk.Label(self, text='Recommendation Product: %s'%product, font=("Times", 12))
        self.label5.grid(row=3, column=1, padx=10, pady=10)
        self.button = tk.Button(self,command=self.closeshow,text="Return",width=20)
        self.button.grid(row=4,column=1)

    def closeshow(self):
        self.label1.grid_forget()
        self.label3.grid_forget()
        self.label5.grid_forget()
        self.button.grid_forget()
        self.id_Button.pack()

    def id_search(self):
        self.label = tk.Label(self,text='Please Enter CustomerID: ',font=("Times",12))
        self.label.pack(pady=50)
        self.pred_e = tk.Entry(self,width=24)
        self.pred_e.pack(pady=50)
        self.Button1 = tk.Button(self,text='Search',font=("Times",12),command=self.show_search, width =24,height=2)
        self.Button1.pack(padx=5)
        self.id_Button.pack_forget()

    def show_search(self):
        self.id = int(self.pred_e.get())
        df = pd.read_csv('Pred.csv',encoding='UTF-8')
        data = pd.DataFrame(columns={"pred_id", "result"})
        # data = pd.DataFrame({"pred_id", "result"})
        for index in df.index:
            if self.id != '':
                if self.id == df['pred_id'].get(index):
                    pred_id = df['pred_id'].get(index)
                    result = df['target'].get(index)
                    new = pd.DataFrame({'pred_id': pred_id, 'result': result}, index=[1])
                    data = data.append(new)
        pre = data.iloc[0][1]
        res = data.iloc[0][0]
        str1 = str(pre)
        str2 = str(res)
        if int(res) == 1:
            str2 = 'High Possiblity'
        elif int(res) == 0:
            str2 = 'Low Possiblity'
        self.closeit()
        if int(res) == 0:
            self.reslut ='Basic Plan'
        else:
            self.reslut ='Premium Plan'
        self.showit(str1,str2,self.reslut)

class PlotFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.plot_Button = tk.Button(self, text='Show Plot', font=("Times", 12), height=2, command=self.show_plot)
        self.plot_Button.pack()

    def show_plot(self):
        window = tk.Tk()
        window.title('Plot of Prediction')
        window.geometry('450x300+480+300')
        frame = tk.Frame(window)
        frame.pack()
        figure_l = plt.figure(figsize=(4, 6))
        figure_l.add_subplot(1, 1, 1)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        csv = pd.read_csv('Pred.csv')
        i = 0
        j = 0
        for index in csv.index:
            if 1 == csv['target'].get(index):
                i = i + 1
        for index in csv.index:
            if 0 == csv['target'].get(index):
                j = j + 1
        y = [j, i]
        x = ['Low Prob', 'High Prob']
        plt.bar(x, y)
        plt.title('Prediction')

        canvas_l = FigureCanvasTkAgg(figure_l, frame)
        canvas_l.draw()
        canvas_l.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

class StoreFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.plot_Button = tk.Button(self, text='Store Start', font=("Times", 12), height=2, command=self.store_files)
        self.plot_Button.pack()

    def store_files(self):
        client = pymongo.MongoClient('mongodb://localhost:27017')
        db = client["db1119"]
        collections = db["Prediction"]
        csv = pd.read_csv('Pred.csv')
        for index in csv.index:
            id = str(csv['pred_id'].get(index))
            age = str(csv['age'].get(index))
            sex = str(csv['sex'].get(index))
            cp = str(csv['cp'].get(index))
            tr = str(csv['trestbps'].get(index))
            ch = str(csv['chol'].get(index))
            fb = str(csv['fbs'].get(index))
            re = str(csv['restecg'].get(index))
            th = str(csv['thalach'].get(index))
            ex = str(csv['exang'].get(index))
            old = str(csv['oldpeak'].get(index))
            sl = str(csv['slope'].get(index))
            ca = str(csv['ca'].get(index))
            tha = str(csv['thal'].get(index))
            ta = str(csv['target'].get(index))
            collections.insert_one(
                {'ID': id, 'Age': age, 'Sex': sex, 'Cp': cp, 'Trestbps': tr, 'Chol': ch, 'Fbs': fb, 'Restecg': re,
                 'Thalach': th, 'Exang': ex, 'Oldpeak': old, 'Slope': sl, 'Ca': ca, 'Thal': tha, 'Prediction': ta})
        tk.messagebox.showinfo('Finished', 'Storage Complete.')

