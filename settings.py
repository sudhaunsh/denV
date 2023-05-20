import tkinter 
import customtkinter
f = open("settings.atom","r")
settings = f.read()
f.close()

settings = settings.split("\n")
Theme = settings[0]
Accent = settings[1]

customtkinter.set_appearance_mode(Theme)  
customtkinter.set_default_color_theme(Accent)

def sett():
    f = open("settings.atom","w")
    f.write(theme.get()+"\n"+Accent.get())
    f.close()
    settings.destroy()

settings = customtkinter.CTk()
settings.geometry("275x200")
settings.title("Settings")

Frame1 = customtkinter.CTkFrame(settings)
Frame1.grid(row = 0, column = 0, padx = 10, pady = 10)

Accent  = customtkinter.CTkOptionMenu(master = Frame1,values = ["blue","green"])
Accent.grid(row = 0, column = 1, padx = 10, pady = 10)

theme = customtkinter.CTkOptionMenu(Frame1,values = ["light","dark","system"])
theme.grid(row = 1, column = 1, padx = 10, pady = 10)

label1 = customtkinter.CTkLabel(Frame1,text = "Restart the application to apply changes")
label1.grid(row = 3, column = 1, padx = 10, pady = 10)

save = customtkinter.CTkButton(Frame1,text = "Save",command = sett)
save.grid(row = 2, column = 1, padx = 10, pady = 10)

settings.mainloop()