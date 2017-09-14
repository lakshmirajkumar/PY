import Tkinter as tk
import MySQLdb


db = MySQLdb.connect("localhost","root","1234","datagrid")
cursor = db.cursor()


def zipsrch():
	print var.get()	
	

def select():
    sf = " %s FILTERING " % var.get()
    root.title(sf)
    if "ZIP" in var.get():
	print var.get()
	tk.Label(root, text="ENTER ZIP ").place(relx=0.2, rely=0.2)
	var.set('500001')
	tk.Entry(root,textvariable = var).place(relx=0.4, rely=0.2)
	tk.Button(root, text="SEARCH", command=zipsrch).place(relx=0.4, rely=0.4, width = 70)
	

    if "NUMBER" in var.get():
	print var.get()
    if "DATE OF BIRTH" in var.get():
	print var.get()
	    

root = tk.Tk()
root.geometry("500x250")
root.title("SEARCHING TOOL")
var = tk.StringVar(root)
var.set('ZIP')
choices = ['ZIP', 'NUMBER', 'DATE OF BIRTH']

tk.OptionMenu(root, var, *choices).place(relx=0.2, rely=0.01, width = 200)

tk.Button(root, text="OK", command=select).place(relx=0.6, rely=0.01, width = 50)


root.mainloop()
