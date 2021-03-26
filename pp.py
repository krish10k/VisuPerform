from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

root = Tk()
root.geometry("500x500+400+400")
root.title("Report Generator")

def f1():
	try:
		name = ent_name.get()
		phy = int(ent_phy.get())
		chem = int(ent_chem.get())
		maths = int(ent_maths.get())
		subject = ['Physics', 'Chemistry', 'Maths']
		marks = [phy,chem,maths]

		plt.plot(subject,marks,linewidth=3)
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(name+"s Performance")
		plt.show()
		
		plt.bar(subject,marks,linewidth=3)
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(name+"s Performance")
		plt.show()
       
		plt.pie(marks, labels=subject, autopct='%.2f%%', shadow=True)
		plt.show()
	
	except ValueError:
		showerror("Mistake",'invalid marks')
		ent_phy.delet(0, END)
		ent_chem.delet(0, END)
		ent_maths.delet(0, END)
		ent_phy.focus()
	

	

f = ('Calibri', 20, 'bold')
lbl_name = Label(root, text="Name Of Student", font=f,)
ent_name = Entry(root, bd=5, font=f)
lbl_phy = Label(root, text="Physics Marks", font=f,)
ent_phy = Entry(root, bd=5, font=f)
lbl_chem = Label(root, text="Chemistry Marks", font=f,)
ent_chem = Entry(root, bd=5, font=f)
lbl_maths = Label(root, text="Mathematics Marks", font=f,)
ent_maths = Entry(root, bd=5, font=f)

lbl_name.pack(pady=3)
ent_name.pack(pady=3)
lbl_phy.pack(pady=3)
ent_phy.pack(pady=3)
lbl_chem.pack(pady=3)
ent_chem.pack(pady=3)
lbl_maths.pack(pady=3)
ent_maths.pack(pady=3)

btn_line = Button(root, text="Result Analysis", font=f, width=15, command=f1).pack(pady=10)


root.mainloop()