from tkinter import *
from tkinter import ttk
import tkinter.messagebox
root = Tk()

#setting หน้าจอ
root.title("Temperature Converter Program")
root.iconbitmap(r'D:\Tkinker Kongsaksayam\TempConverter Asset\tempicon.ico')
# root.geometry("500x500+500+70")
root.config(bg="#f7fcff")
font=("Arial Narrow",14)
Label(root,text="Welcome to Temperature Converter",font=font,bg="#f7fcff").pack(padx=5,pady=5)

#setting Frame
input_frame = Frame(root,bg="#FDFF9C")
input_frame.pack(padx=5,pady=5,ipadx=40,fill=X,expand=True)

calculate_frame = Frame(root,bg="#88FFC5")  
calculate_frame.pack(padx=5,pady=5,ipadx=40,fill=X,expand=True)

output_frame = Frame(root,bg="#FF97CB")
output_frame.pack(padx=5,pady=5,ipadx=40,fill=X,expand=True)

#variable
inputData = StringVar()
choice = IntVar()
temp = StringVar()

#input widget
text1 = Label(input_frame,text="Temperature (Celcius)",font=font)
text1.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=5,sticky=W)
input = Entry(input_frame,bg="white",textvariable=inputData,font=font)
input.grid(row=0,column=1,ipadx=20)

#def @choice widget
def Select():
    if choice.get() ==1:
        print("Kelvin")
    elif choice.get() ==2:
        print("Fahrenheit")
    else :
        tkinter.messagebox.showerror("Error","You did not fill yet")
        
# choice widget 
text2 = Label(calculate_frame,text="Convert into",font=font)
text2.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=5)

check1 = ttk.Checkbutton(calculate_frame,text="Kelvin",onvalue=1,offvalue=0,variable=choice,command=Select).grid(row=0,column=1,padx=5,pady=5,ipadx=10,ipady=10)
check2 = ttk.Checkbutton(calculate_frame,text="Fahrenheit",onvalue=2,offvalue=0,variable=choice,command=Select).grid(row=0,column=2,padx=5,pady=5,ipadx=10,ipady=10)
check3 = ttk.Checkbutton(calculate_frame,text="none",onvalue=3,offvalue=0,variable=choice,command=Select).grid(row=0,column=3,padx=5,pady=5,ipadx=10,ipady=10)

#combobox widget
# unit_label = Label(root,text="Change into",font=font)
# unit_list = ["Kelvin","Fahrenheit"]
# temp_combo = ttk.Combobox(root,value=unit_list,font=font)
# temp_combo.set("Kelvin")
# unit_label.grid(row=1,column=0,sticky=W)
# temp_combo.grid(row=1,column=1)


#def @output widget
def showTemp():
    showResult.delete(0,END)
    A = float(inputData.get())
    B = choice.get()
    if B == 1: #Cel to Kel
        tempKel = A + 273.15
        showResult.insert(0,tempKel)
    elif B== 2 : #Cel to Fah
        tempFah = (A*(9/5))+32
        showResult.insert(0,tempFah)
    
def clearData():
    input.delete(0,END)
    showResult.delete(0,END)
    choice.set(0)
    
#output widget @ output_frame
outPut = Label(output_frame,text="Result",font=font)
outPut.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=5)
showResult = Entry(output_frame,bg="white",font=font)#,textvariable=temp
showResult.grid(row=0,column=1,padx=5,pady=5,ipadx=100,ipady=5)

#button widget @ output_frame
changBut = Button(output_frame,text="Change",bg="#8CDDFE",font=font,command=showTemp) 
changBut.grid(row=1,column=0,sticky=W,padx=5,pady=5)
clearBut = Button(output_frame,text="Clear",bg="#8CDDFE",font=font,command=clearData) 
clearBut.grid(row=1,column=1,sticky=E,padx=5,pady=5)

root.mainloop() 