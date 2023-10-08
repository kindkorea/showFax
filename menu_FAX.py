import tkinter
import os
import glob







window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

frame=tkinter.Frame(window, 
                    width=300,
                    )

scrollbar=tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


def is_check_v(filename):
    print(os.path.basename(filename))

def items_selected(event):

    selected_indices = listbox.curselection()
    print(f'{selected_indices=}')
    msg = listbox.get(selected_indices[0])
    is_check_v(msg)

def items_doubleClicked(event):
    selected_indices = listbox.curselection()
    msg = listbox.get(selected_indices[0])
    os.system(f'./img/{msg}')


listbox=tkinter.Listbox(frame, 
                        yscrollcommand = scrollbar.set,
                        # listvariable=var,
                        width=100,
                        )

listbox.pack(side="left")


listbox.bind('<<ListboxSelect>>', items_selected)
listbox.bind('<Double-Button-1>',items_doubleClicked)

scrollbar["command"]=listbox.yview

frame.pack()


chk_active = tkinter.IntVar()



frame2 =tkinter.Frame(window, 
                    width=300,
                    )

def get_file():
    src_path = './img'
    load_files = glob.glob(src_path+'/*.*')
    return  [file for file in load_files if file.endswith('.jpg')]

def all_files():
    listbox['listvariable'] = tkinter.Variable(value=get_file())

def noCheck_files():
    noChk_file_list = [file for file in get_file() if os.path.basename(file)[0] != 'v']
    listbox['listvariable'] = tkinter.Variable(value=noChk_file_list)

def checked_files():
    noChk_file_list = [file for file in get_file() if os.path.basename(file)[0] == 'v']
    listbox['listvariable'] = tkinter.Variable(value=noChk_file_list)

btn_all_files = tkinter.Button(frame2, text='모든파일' ,command=all_files)
btn_noCheck_files = tkinter.Button(frame2, text='미확인파일', command=noCheck_files)
btn_Checked_files = tkinter.Button(frame2, text='확인파일', command=checked_files)


frame3 =tkinter.Frame(window, 
                    width=300,
                    )

chk_button = tkinter.Checkbutton(frame3,text='확인' , variable=chk_active)



chk_button.pack()
btn_all_files.pack()
btn_noCheck_files.pack(side='right')
btn_Checked_files.pack(side='left')
# chk_button.select()

frame2.pack()
frame3.pack()
print(f'{chk_active.get()}')



window.mainloop()