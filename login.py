from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='dharma'and passwordEntry.get()=='1909':
        messagebox.showinfo('success','login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid credentials')
root=CTk() #creating window using CTk class
root.geometry('930x478') # specifying window width and height
root.resizable(0,0) #specifying that it can not be resized
root.title('Login Page') #adding title to the window
image=CTkImage(Image.open('login-page.jpg'),size=(930,478)) #importing image 
imageLabel=CTkLabel(root,image=image,text='') #creating a imagelabel to add it yo window if we dont specify text='' we will be getting CTk label text in the window
imageLabel.place(x=0,y=0) #specifies the position of image
headingLabel=CTkLabel(root,text='Employee Management System',bg_color='#232e30',font=('Goudy Old Style',20,'bold'))
headingLabel.place(x=20,y=100)
usernameEntry=CTkEntry(root,placeholder_text='Enter your Username',width=180) #entry field creation
usernameEntry.place(x=50,y=180)
passwordEntry=CTkEntry(root,placeholder_text='Enter your password',width=180,show='*')
passwordEntry.place(x=50,y=230)
loginbutton=CTkButton(root,text='Login',cursor='hand2',command=login) #button creation ,command allows to specify function
loginbutton.place(x=70,y=280)
root.mainloop() # to make it run infinitely