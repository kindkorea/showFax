import os
import subprocess
import glob
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

src_path = './img'
# print(f'{src_path=}')
load_files = glob.glob(src_path+'/*.*')
jpg_file_list = [file for file in load_files if file.endswith('.jpg')]

# for file in jpg_file_list : 

noChk_file_list = [file for file in jpg_file_list if os.path.basename(file)[0] != 'v']
print(f'{noChk_file_list=}')



# for file in noChk_file_list:
#     print(f'{file=}')
#     subprocess.run(f'C:/Users/kindk/AppData/Local/Imagine/Imagine64.exe {file}')

# create the root window
root = tk.Tk()
root.title('Listbox')
# root.geometry("600x600")

# create a list box
# langs = ('Java', 'C#', 'C', 'C++', 'Python',
#          'Go', 'JavaScript', 'PHP', 'Swift')



var = tk.Variable(value=noChk_file_list)

frame = tk.Frame(root)


listbox = tk.Listbox(
    frame,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.pack(expand=True, fill=tk.BOTH)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    frame,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)


def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    # showinfo(title='Information', message=msg)
    print(msg)


listbox.bind('<<ListboxSelect>>', items_selected)
frame.pack()
root.mainloop()