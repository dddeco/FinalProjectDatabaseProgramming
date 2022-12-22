import tkinter as tk
from View import AboutFrame,SearchFrame,PlotFrame,StoreFrame

class MainPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Recommendation System ver1.0')
        self.root.geometry('600x400+400+200')
        self.create_page()
        self.search_frame = SearchFrame(self.root)
        self.about_frame = AboutFrame(self.root)
        self.plot_frame = PlotFrame(self.root)
        self.store_frame = StoreFrame(self.root)
        #self.root.mainloop()

    def create_page(self):
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Search', command=self.show_search)
        menubar.add_command(label='Plot', command=self.show_plot)
        menubar.add_command(label='Store', command=self.show_store)
        menubar.add_command(label='About', command=self.show_about)
        self.root['menu'] = menubar

    def show_about(self):
        self.about_frame.pack()
        self.search_frame.pack_forget()
        self.plot_frame.pack_forget()
        self.store_frame.pack_forget()
        pass

    def show_search(self):
        self.about_frame.pack_forget()
        self.search_frame.pack()
        self.plot_frame.pack_forget()
        self.store_frame.pack_forget()
        pass

    def show_plot(self):
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()
        self.plot_frame.pack()
        self.store_frame.pack_forget()
        pass

    def show_store(self):
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()
        self.plot_frame.pack_forget()
        self.store_frame.pack()
        pass
