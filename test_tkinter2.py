import tkinter as tk


class Gui_list :

    def __init__ (self,window,x,y) :
        self.root = window
        self.frame = tk.Frame(self.root,
                            #   text='FAX folder',
                            padx=10,
                            pady=10
                            )
        self.positionX = x
        self.positionY = y


    def tk_run(self) :
        listbox = tk.Listbox(
            self.frame,
            # listvariable=var,
            height=6,
            # selectmode=tk.EXTENDED
        )
        listbox.pack()
        self.frame.pack(side='left',
                        fill='both',
                        expand=True)



    