import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
import sympy

class OC_Calculator(Frame):

    def __init__(self, master): 
        super().__init__(master)    
        # self.parent = parent
        # self.frame = Frame(self.parent)
        # self.frame.pack()
        self.initialize()

    def initialize(self):
        self.calc_result = StringVar()
        self.entry = Entry(self,  textvariable=self.calc_result )
        
        self.entry.bind('<Return>', self.cal)
       
        self.btn = Button(self, text='run',  command=self.cal)
        self.btn.pack()
        self.entry.pack()


    def cal(self,event):
        a = self.entry.get()
        result = sympy.sympify(a)
        self.entry.delete(0,END)
        print(result)
        self.calc_result.set(result) 
root = Tk()
root.geometry("300x200")
app = OC_Calculator(root)

root.mainloop()