import customtkinter as ck
from CTkListbox import *
import scan_nmap 


#---- Functions

def scanTarget():
    global Target
    temp = targetTextBox.get()
    if temp != '':
        Target = temp
        scan_nmap.scanTarget(Target)
    else:
        pass

#------- Global Var

Target = ''

#----- Buid Gui
ck.set_appearance_mode("dark")  # Modes: system (default), light, dark
ck.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = ck.CTk()  # create CTk window like you do with the Tk window
app.geometry("1200x700")
app.title('GODEYE')

  #Target 
targetTextBox = ck.CTkEntry(app,width=300)
targetTextBox.place(relx=0.6, rely=0.05, anchor=ck.NE)
#ScanButton
scanButton = ck.CTkButton(app,width=10,text='S',command=scanTarget)
scanButton.place(relx=0.62, rely=0.05, anchor=ck.NE)
#domains
dominLabel = ck.CTkLabel(app,text='Domains')
dominLabel.place(relx=0.1, rely=0.2, anchor=ck.NE)
domainsListBox = CTkListbox(app)
domainsListBox.place(relx=0.15, rely=0.25, anchor=ck.NE)
#services
servicesLabel = ck.CTkLabel(app,text='Services')
servicesLabel.place(relx=0.3, rely=0.2, anchor=ck.NE)
servicesListBox = CTkListbox(app)
servicesListBox.place(relx=0.35, rely=0.25, anchor=ck.NE)
#dorks


# def mainGui(app):
#     #Target 
#     targetTextBox = ck.CTkEntry(app,width=300)
#     targetTextBox.place(relx=0.6, rely=0.05, anchor=ck.NE)
#     #ScanButton
#     scanButton = ck.CTkButton(app,width=10,text='S',command=scanTarget)
#     scanButton.place(relx=0.62, rely=0.05, anchor=ck.NE)
#     #domains
#     dominLabel = ck.CTkLabel(app,text='Domains')
#     dominLabel.place(relx=0.1, rely=0.2, anchor=ck.NE)
#     domainsListBox = CTkListbox(app)
#     domainsListBox.place(relx=0.15, rely=0.25, anchor=ck.NE)
#     #services
#     servicesLabel = ck.CTkLabel(app,text='Services')
#     servicesLabel.place(relx=0.3, rely=0.2, anchor=ck.NE)
#     servicesListBox = CTkListbox(app)
#     servicesListBox.place(relx=0.35, rely=0.25, anchor=ck.NE)
#     #dorks


def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# mainGui(app)

app.mainloop()