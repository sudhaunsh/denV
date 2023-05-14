import tkinter
from typing import Optional, Tuple, Union
import customtkinter 
from back_end import*
from report_gen import*
from advisory import*
import os 
from PIL import Image
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")
image_path = os.path.join(os.path.dirname(__file__), "img")
logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "power.png")),size = (150,30))
prediction_txt = "Run to generate predictions"
advisory = "Run to generate advisory"
app = customtkinter.CTk()
app.geometry("1000x800")
app.title("DenV advisor")
status = "idle"
Name = ""
PDF_state = 0
compli = False 
Count1 = 0
Count2 = 0

def  pdf_gen():
    global PDF_state
    if PDF_state == 0:
        PDF_state = 1
    elif PDF_state == 1:
        PDF_state = 0
    print(PDF_state)

def compli_state():
    compli = True

def verify_entry(verify_val):
    Name = str(verify_val[0])
    Count1 = str(verify_val[0])
    Count2 = str(verify_val[0])
    Age = str(verify_val[0])
    Date_onset = str(verify_val[0])
    Date1 = str(verify_val[0])
    Date2 = str(verify_val[0])
    verify = True

    try:
        Count1 = float(Count1)
        Count2 = float(Count2)
        Age = float(Age)
    except:
        verify = False
    len_chk = [len(Name),len(Count1),len(Count2),len(Age),len(Date_onset)]
    if 0 in len_chk:
        verify = False 
    else:
        verify = True
    return verify

def process():
    Name = str(name.get())
    Count1 = str(count1.get())
    Count2 = str(count2.get())
    Age = str(age.get())
    Date_onset = str(date_onset.get())
    Date1 = str(date1.get())
    Date2 = str(date2.get())
    verify_val = {0:Name,1:Count1,2:Count2,3:Age,4:Date_onset,5:Date1,6:Date2}
    print(verify_val)
    verify = verify_entry(verify_val)
    if verify == False:
        status = "Please check your entry"
        stat.configure(text=status)
    else: 
        status = "Complete"
        stat.configure(text=status)
        #Run back end 
    #/////////////move ->    
    x0 = [1,2,3,4,5,6,7,8,9,10,11]
   
    result = estimate(verify_val)
    pat_data1 = result[2]
    pat_data2 = result[3]
    confidence = result[4]
    plot_data = {0:x0,1:pat_data1,2:pat_data2}
    plot_grph(plot_data)
    lc = float(np.min(pat_data2))
    advice = advise(lc)
    if PDF_state == 1:
        pat_data = {0:pat_data1,1:pat_data2,2:Name,3:Age,4:Date_onset,5:confidence,6:count1,7:count2}
        generate_report(pat_data)


def plot_grph(plot_data):
    x = plot_data[0]
    y = plot_data[1]
    y1 = plot_data[2]
    plot1.plot(x,y,label = "Platelet count 1")
    plot1.plot(x,y1,label = "Platelet count 2")
    plot1.legend()
    canvas.draw()
    

Frame1 = customtkinter.CTkFrame(master = app,width = 500, height = 800,corner_radius=5)
Frame1.grid(row = 0, column = 0)

Frame2 = customtkinter.CTkFrame(master = app,width = 500, height = 800,corner_radius=5)
Frame2.grid(row = 0, column = 1)

labelname = customtkinter.CTkLabel(master=Frame1,text="Please enter patient name")
labelname.pack(pady = 10,padx = 10,fill="both",expand=False)

name = customtkinter.CTkEntry(master=Frame1,placeholder_text="Name")
name.pack(pady = 10, padx = 10, fill="both",expand = False)

labelage = customtkinter.CTkLabel(master = Frame1,text="Please enter patient's age")

age = customtkinter.CTkEntry(master = Frame1,placeholder_text="Age")
age.pack(pady=10, padx=10, fill="both", expand=False)

labelonset = customtkinter.CTkLabel(master = Frame1, text="Please enter date of onset of symptoms")
labelonset.pack(pady=10, padx=10, fill="both", expand=False)

date_onset = customtkinter.CTkEntry(master = Frame1, placeholder_text="dd\mm\YY")
date_onset.pack(pady=10, padx=10, fill="both", expand=False)

label2 = customtkinter.CTkLabel(master=Frame1,text="Enter the first platelet count details")
label2.pack(pady = 10,padx = 10,fill="both",expand=False)

count1 = customtkinter.CTkEntry(master = Frame1, placeholder_text="1st platelet count in thousand")
count1.pack(pady=10, padx=10, fill="both", expand=False)

date1 = customtkinter.CTkEntry(master = Frame1, placeholder_text="What day was the test done post onset")
date1.pack(pady=10, padx=10, fill="both", expand=False)

label3 = customtkinter.CTkLabel(master=Frame1,text="Enter the second platelet count")
label3.pack(pady = 10,padx = 10,fill="both",expand=False)

count2 = customtkinter.CTkEntry(master = Frame1, placeholder_text="2nd platelet count in thousand")
count2.pack(pady=10, padx=10, fill="both", expand=False)

date2 = customtkinter.CTkEntry(master = Frame1, placeholder_text="What day was the test done post onset")
date2.pack(pady=10, padx=10, fill="both", expand=False)

option_menu = customtkinter.CTkOptionMenu(master=Frame1,values = ['Please select day for prediction','0','1','2','3','4','5','6','7','8','9','10','11'])
option_menu.pack(pady=10, padx=10, fill="both", expand=False)

complications = customtkinter.CTkCheckBox(master = Frame1, text = "Are any medical complications observed?",command=compli_state)
complications.pack(pady=10, padx=10, fill="both", expand=False)

pdf_chkbok = customtkinter.CTkCheckBox(master = Frame1, text="Generate PDF report",command = pdf_gen)
pdf_chkbok.pack(pady=10, padx=10, fill="both", expand=False)

run = customtkinter.CTkButton(master = Frame1,text = "Run",command=process)
run.pack(pady=10, padx=10, fill="both", expand=False)

stat = customtkinter.CTkLabel(master=Frame1,text = status)
stat.pack(pady=10, padx=10, fill="both", expand=False)

label1 = customtkinter.CTkLabel(master = Frame1, image = logo,text = "")
label1.pack(pady = 10,padx = 10,fill="both",expand=False)

label_prediction = customtkinter.CTkLabel(master=Frame2,text = prediction_txt)
label_prediction.pack(pady = 10,padx = 10,fill="both",expand=False)

label_advisory = customtkinter.CTkLabel(master=Frame2,text = advisory)
label_advisory.pack(pady = 10,padx = 10,fill="both",expand=False)

fig = Figure(figsize = (6, 5),dpi = 100)
plot1 = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig,Frame2)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app.mainloop()