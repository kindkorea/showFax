# import tkinter as tk
# import test_tkinter2



# root = tk.Tk()
# root.title('Listbox')
# root.geometry('600x300')
# # gui_list=test_tkinter2.Gui_list(root,10,10)
# # gui_list.tk_run()

# frame = tk.Frame(root, relief='solid', bd=2)
# frame.pack(side='right', fill='both')


# # frame1=tkinter.Frame(window, relief="solid", bd=2)
# # frame1.pack(side="left", fill="both", expand=True)


# root.mainloop()


from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()

