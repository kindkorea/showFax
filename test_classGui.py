import tkinter

class SimpleApp(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.initialize()
        # print(self.parent)


    def initialize(self):
        # self.grid()

        # 입력창
        self.entryValue = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryValue)
        self.entry.grid(column=0, row=0, sticky='WE')
        self.entry.bind('<Return>', self.onPressEnter)

        # 버튼
        button = tkinter.Button(self, text='클릭',
                                command=self.onButtonClick)
        button.grid(column=1, row=0)

        # 이름표
        self.labelValue = tkinter.StringVar()
        self.label = tkinter.Label(self, fg='white', bg='orange',
                                   textvariable=self.labelValue)
        self.label.grid(column=0, row=1, columnspan=2, sticky='EW')

        # 초기값
        self.entryValue.set('hello python')
        self.labelValue.set('empty')

        self.entry.focus_set()
        self.entry.select_range(0, tkinter.END)

        self.geometry('200x200+500+300')

    def onPressEnter(self, event):
        print('enter')

        self.labelValue.set(self.entryValue.get() + '[return]')
        self.entryValue.set('')

    def onButtonClick(self):
        print('button')

        self.labelValue.set(self.entryValue.get() + '[button]')


app = SimpleApp(None)
# app.title = '그래픽 유저 인터페이스'
app.title('hello')
app.mainloop()