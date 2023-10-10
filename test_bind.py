import tkinter

class SimpleApp():

    def __init__(self, parent):
        
        self.parent = parent

        self.frame = tkinter.Frame(self.parent)
        self.initialize()
        self.frame.pack(side='top')

    def initialize(self):
        # self.grid()

        # 입력창
        self.entryValue = tkinter.StringVar()
        self.entry = tkinter.Entry(self.frame, textvariable=self.entryValue)
        self.listbox = tkinter.Listbox(self.frame)
        
        self.entry.grid(column=0, row=0, sticky='WE')
        self.listbox.grid(column=0,row=3)
        self.entry.bind('<Button-1>', self.onPressEnter)

        # self.listbox.bind('<Button-1>', self.items_selected)
        # 버튼
        button = tkinter.Button(self.frame, text='클릭',
                                command=self.onButtonClick)
        button.grid(column=1, row=0)

        # 이름표
        self.labelValue = tkinter.StringVar()
        self.label = tkinter.Label(self.frame, fg='white', bg='orange',
                                   textvariable=self.labelValue)
        self.label.grid(column=0, row=1, columnspan=2, sticky='EW')

        # 초기값
        self.entryValue.set('hello python')
        self.labelValue.set('empty')

        self.entry.focus_set()
        self.entry.select_range(0, tkinter.END)

        # self.geometry('200x200+500+300')

    def onPressEnter(self, event):
        print('enter')
        self.labelValue.set(self.entryValue.get() + '[return]')
        self.entryValue.set('')

    def onButtonClick(self):
        print('button')

        self.labelValue.set(self.entryValue.get() + '[button]')


class SimpleApp2():

    def __init__(self, parent):
       

        self.parent = parent

        self.frame = tkinter.Frame(self.parent)
        self.initialize()
        self.frame.pack(side='bottom')

    def initialize(self):
        # self.grid()

        # 입력창
        self.entryValue = tkinter.StringVar()
        self.entry = tkinter.Entry(self.frame, textvariable=self.entryValue)
        self.listbox = tkinter.Listbox(self.frame)
        
        self.entry.grid(column=0, row=0, sticky='WE')
        self.listbox.grid(column=0,row=3)
        self.entry.bind('<Button-1>', self.onPressEnter)

        # self.listbox.bind('<Button-1>', self.items_selected)
        # 버튼
        button = tkinter.Button(self.frame, text='클릭',
                                command=self.onButtonClick)
        button.grid(column=1, row=0)

        # 이름표
        self.labelValue = tkinter.StringVar()
        self.label = tkinter.Label(self.frame, fg='white', bg='orange',
                                   textvariable=self.labelValue)
        self.label.grid(column=0, row=1, columnspan=2, sticky='EW')

        # 초기값
        self.entryValue.set('hello python')
        self.labelValue.set('empty')

        self.entry.focus_set()
        self.entry.select_range(0, tkinter.END)

        # self.geometry('200x200+500+300')

    def onPressEnter(self, event):
        print('enter')
        self.labelValue.set(self.entryValue.get() + '[return]')
        self.entryValue.set('')

    def onButtonClick(self):
        print('button')

        self.labelValue.set(self.entryValue.get() + '[button]')

root = tkinter.Tk()

app = SimpleApp(root)
app2 = SimpleApp2(root)
root.title = '그래픽 유저 인터페이스'
root.geometry("600x500")
root.mainloop()