from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database
import re
def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        PhoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def is_valid_phone_number(phone):
    return bool(re.fullmatch(r"[6-9]\d{9}", phone))

def new_employee():
    clear(True)

def add_employee():
    if idEntry.get() == '' or PhoneEntry.get() == '' or nameEntry.get() == ''or salaryEntry.get() == '':
        messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    elif len(idEntry.get())>6:
        messagebox.showerror('Error','Id cannot be more than 6 digits long')
    elif len(nameEntry.get()) < 2:
        messagebox.showerror('Error','Name must be atleast two characters long')
    elif len(PhoneEntry.get()) != 10:
        messagebox.showerror('Error','Phone number must be 10 digits')
    elif not is_valid_phone_number(PhoneEntry.get()):
        messagebox.showerror('Error','Phone number must start with digits [6-9]')
    else:
        database.insert(idEntry.get(),nameEntry.get(),PhoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data added successfully')

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),PhoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data Updated successfully')

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data Deleted successfully')

def delete_all_employee():
    value = messagebox.askyesno('Confirm','Do you really wnat to delete all the records')
    if value:
        database.deleteall()
        treeview_data()
        clear()
        messagebox.showinfo('Success','All records are deleted')

def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error','Please select a option to search')
    else:
        searchdata = database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searchdata:
            tree.insert('',END,values=employee)

def showall():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

window=CTk()
window.geometry('1020x580')
window.resizable(0,0)
window.title('Employee Management System')
window.configure(fg_color="#160C30")

logo=CTkImage(Image.open('pic2.png'),size=(1020,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=3)

leftFrame=CTkFrame(window,fg_color="#160C30")
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')
idEntry=CTkEntry(leftFrame,width=180)
idEntry.grid(row=0,column=1)
nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')
nameEntry=CTkEntry(leftFrame,width=180)
nameEntry.grid(row=1,column=1)
phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')
PhoneEntry=CTkEntry(leftFrame,width=180)
PhoneEntry.grid(row=2,column=1)
roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=['web developer','Data analyst','Techinal writer','Network Engineer','IT consultant','UI/UX designer']
roleBox=CTkComboBox(leftFrame,values=role_options,font=('arial',15,'bold'),width=180,state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])
genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,font=('arial',15,'bold'),width=180,state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Male')
salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')
salaryEntry=CTkEntry(leftFrame,width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

search_options=['Id','Name','Role','Phone','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')
searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)
searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)
showallButton=CTkButton(rightFrame,text='Show all',width=100,command=showall)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4,pady=5,padx=5)
tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('Id',width=100)  #anchor=CENTER 
tree.column('Name',width=160)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=140)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowheight=25,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color="#160C30")
buttonFrame.grid(row=2,column=0,columnspan=5,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=new_employee)
newButton.grid(row=0,column=0,padx=5,pady=5)
addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,padx=5,pady=5)
updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,padx=5,pady=5)
deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,padx=5,pady=5)
deleteallButton=CTkButton(buttonFrame,text='Delete all Employees',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all_employee)
deleteallButton.grid(row=0,column=4,padx=5,pady=5)

treeview_data()
window.bind('<ButtonRelease>',selection)
window.mainloop()