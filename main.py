import menu_convertor
import menu_FAX
import tkinter


root = tkinter.Tk()


root.title("OC PROGRAMS")
# root.ttk.call('wm','./icon.png')
# icon = PhotoImage(file='./icon.png ')
# root.wm_iconphoto(False, icon)

app1 = menu_convertor.PDFconvert(root)
app2 = menu_FAX.MenuFax(root)

root.resizable(True, True)
root.geometry("500x700+2000+10")
root.mainloop()
