
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
import sympy



root = Tk()

widget_list = {}

def cmd(e,column):
    # entry = e.widget
    # for widget in widget_list:
        #   print(f'{widget=}')
        #   print(f'{entry=}')
        #   if widget is entry : 
                # print(type(entry))
                # print(type(widget))
    print(column)


def make_entry(frame, row, column, width, text, state):
        e = Entry(frame, width=width)
        if text: e.insert(0, text)
        e['state'] = NORMAL if state else DISABLED
        e.coords = (row-1, column-1)
        e.grid(row=row, column=column)
        e.bind('<Return>',lambda : cmd(column), add='hello')
        return e

for i in range(5):
    widget_list[i] = make_entry(root, 0,i,12,'',True)

print(widget_list)

widget_list[2].insert(END,'hello')

root.mainloop()
