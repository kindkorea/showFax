import tkinter as tk


app = tk.Tk()

class Excel(tk.Frame):
    def __init__(self, master, rows, columns, width):
        super().__init__(master)

        
        for i in range(columns):
            self.make_entry(0, i+1, width, f'Margin{i}', False) 

        for row in range(rows):
            self.make_entry(row+1, 0, 5, f'R{row}', False)
                
            for column in range(columns):
                self.make_entry(row+1, column+1, width, '', True)

    def make_entry(self, row, column, width, text, state):
        e = tk.Entry(self, width=width )
        if text: e.insert(0, text)
        
        e['state'] = tk.NORMAL if state else tk.DISABLED
        e.coords = (row-1, column-1)
        e.grid(row=row, column=column)

ex = Excel(app, rows=5, columns=10, width=8)
ex.pack(padx=20, pady=20)

ex2 = Excel(app, rows=3, columns=5, width=20)
ex2.pack(padx=20, pady=20)

def show_cells():
    print('\n--== dumping cells ==--')
    # print(f'{ex.children}')
    for e in ex.children:
        v = ex.children[e]
        v.insert(tk.END,'hello')
        print(f'{v.get()}', end=', ')

    print()


def set_cells():
    print('\n--== dumping cells ==--')
    # print(f'{ex.children}')
    for e in ex.children:
        v = ex.children[e]
        print(f'{v.set()}', end=', ')
    print()


bt = tk.Button(app, text='Dump', command=show_cells)
bt.pack(pady=20)
bt2 = tk.Button(app, text='set', command=set_cells)
bt2.pack(pady=20)

app.mainloop()