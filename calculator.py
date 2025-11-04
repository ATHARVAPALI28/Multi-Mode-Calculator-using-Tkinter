import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk

def mini():
    global md
    if(md=="mini"):
        msg.showinfo("Calculator","Already in mini mode")
    else:
        a=msg.askyesno("Calculator","Do you really want to switch to Mini Mode?")
        if(a==True):
            root.geometry("260x400")
            md="mini"
    
def norm():
    global md
    if(md=="default"):
        msg.showinfo("Calculator","Already in default mode")
    else:
        a=msg.askyesno("Calculator","Do you really want to switch back to Default Mode?")
        if(a==True):
            root.geometry("360x550")
            md="default"

def out():
    a=msg.askyesno("Calculator","Do you really want to Exit?")
    if(a==True):
        root.destroy()

def hlp():
    msg.showinfo("Calculator","Calculator Application Help\n\n"
    "This calculator allows you to perform basic arithmetic operations such as "
    "addition, subtraction, multiplication, and division.\n\n"
    "Menu Options:\n"
    "• View → Switch between Mini and Default window sizes.\n"
    "• Mode → Access special calculators like BMI, GST, and Discount.\n"
    "• Help → View usage instructions and application information.\n\n"
    "Usage Tips:\n"
    "1. Use the on-screen buttons to enter numbers and operators.\n"
    "2. Press '=' to evaluate the expression.\n"
    "3. Click 'C' to clear the input.\n"
    "4. Use the menu bar to explore additional features.\n\n"
    "Developed by: Atharva Pali\n"
    "Version: 1.0.0\n"
    "© 2025 BluecraneEditZ™. All rights reserved.")

def key_event(event):
    key=event.keysym
    if(key in "0123456789"):
        click(key)
    elif(key=="period" or key=="Decimal"):
        click(".")
    elif(key in ["plus","KP_Add"]):
        click("+")
    elif(key in ["minus","KP_Subtract"]):
        click("-")
    elif(key in ["asterisk","KP_Multiply"]):
        click("×")
    elif(key in ["slash","KP_Divide"]):
        click("÷")
    elif(key in ["Return","equal"]):
        click("=")
    elif(key in ["BackSpace"]):
        click("C")
    elif(key.lower()=="c"):
        click("AC")


def bmi():
    def calc_bmi():
        try:
            h=float(height.get())
            w=float(weight.get())
            h=h/100  
            bmi=round((w/(h**2)),2)
            if(bmi<18.5):
                result=f"Your BMI is {bmi} (Underweight)"
            elif(18.5<=bmi<25):
                result=f"Your BMI is {bmi} (Normal)"
            elif(bmi>=25 and bmi<30):
                result=f"Your BMI is {bmi} (Overweight)"
            else:
                result=f"Your BMI is {bmi} (Obese)"
            msg.showinfo("BMI Report",result)
        except(Exception):
            msg.showerror("Error","Enter valid height and weight.")

    win=tk.Toplevel(root)
    win.title("BMI")
    win.config(bg="#1e1e1e")
    win.geometry("300x400")
    win.resizable(False,False)
    tk.Label(win,text="Body Mass Index",font=("Digital-7 Mono",20,"bold"),bg="#1e1e1e",fg="orange").pack(pady=15)
    tk.Label(win,text="Height(cm)",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    height=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    height.pack(pady=5)
    tk.Label(win,text="Weight(kg)",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    weight=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    weight.pack(pady=5)
    tk.Button(win,text="Calculate",font=("Segoe UI",10,"bold"),bg="orange",fg="white",command=calc_bmi).pack(pady=10)

def gst():
    def calc_gst():
        try:
            og=float(original.get())
            val=float(per.get())
            add=(og*val)/100
            gst=add+og
            msg.showinfo("GST",f"Final Price: ₹{gst}\nTax Amount: ₹{add}")
        except(Exception):
            msg.showerror("Error","Enter valid Original Price.")
    win=tk.Toplevel(root)
    win.title("GST")
    win.config(bg="#1e1e1e")
    win.geometry("300x400")
    win.resizable(False,False)
    tk.Label(win,text="Good & Service Tax",font=("Digital-7 Mono",20,"bold"),bg="#1e1e1e",fg="orange").pack(pady=15)
    tk.Label(win,text="Original Price",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    original=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    original.pack(pady=5)
    tk.Label(win,text="GST(%)",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    per=ttk.Combobox(win,font=("Segoe UI",12,"bold"),value=["3","5","12","18","28"],state="readonly",justify="center")
    per.pack(pady=5)
    tk.Button(win,text="Calculate",font=("Segoe UI",10,"bold"),bg="orange",fg="white",command=calc_gst).pack(pady=10)

def discount():
    def calc_disc():
        try:
            og=float(original.get())
            disc=float(discount.get())
            sub=(og*disc)/100
            act=og-sub
            msg.showinfo("Discount",f"Final Price: ₹{act}\nDiscount: ₹{sub}")
        except(Exception):
            msg.showerror("Error","Enter valid Original Price & Discount(%).")
            
    win=tk.Toplevel(root)
    win.title("Discount")
    win.config(bg="#1e1e1e")
    win.geometry("300x400")
    win.resizable(False,False)
    tk.Label(win,text="Discount",font=("Digital-7 Mono",20,"bold"),bg="#1e1e1e",fg="orange").pack(pady=15)
    tk.Label(win,text="Original Price",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    original=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    original.pack(pady=5)
    tk.Label(win,text="Discount(%)",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    discount=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    discount.pack(pady=5)
    tk.Button(win,text="Calculate",font=("Segoe UI",10,"bold"),bg="orange",fg="white",command=calc_disc).pack(pady=10)

def num():
    def calc_num():
        try:
            val=int(dec.get())
            if(not val):
                msg.showerror("Error","Please enter a value.")
                return
            choice=cb1.get()
            if(choice=="Binary"):
                result=bin(val)[2:]
            elif(choice=="Octal"):
                result=oct(val)[2:]
            elif(choice=="Hexadecimal"):
                result=hex(val)[2:].upper()
            else:
                msg.showerror("Error","Invalid Selection.")
                return
            unk.config(state="normal")
            unk.delete(0,tk.END)
            unk.insert(0,result)
            unk.config(state="readonly")
        except(Exception):
            msg.showerror("Error","Enter a valid decimal number.")
            
    win=tk.Toplevel(root)
    win.title("Numeral System")
    win.config(bg="#1e1e1e")
    win.geometry("300x400")
    win.resizable(False,False)
    tk.Label(win,text="Numeral System",font=("Digital-7 Mono",20,"bold"),bg="#1e1e1e",fg="orange").pack(pady=15)
    tk.Label(win,text="Decimal",font=("Segoe UI",12,"bold"),bg="#1e1e1e",fg="white").pack(pady=5,ipadx=5,ipady=5)
    dec=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    dec.pack(pady=5)
    cb1=ttk.Combobox(win,font=("Segoe UI",12,"bold"),value=["Binary","Octal","Hexadecimal"],state="readonly",justify="center")
    cb1.pack(pady=5)
    cb1.current(0)
    unk=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center",state="readonly")
    unk.pack(pady=5)
    tk.Button(win,text="Calculate",font=("Segoe UI",10,"bold"),bg="orange",fg="white",command=calc_num).pack(pady=10)

def temp():
    def calc_temp():
        try:
            val=float(a.get())
            p=cb2.get()
            q=cb3.get()
            if(p==q):
                result=val
            elif(p=="Celsius" and q=="Fahrenheit"):
                result=(val*9/5)+32
            elif(p=="Fahrenheit" and q=="Celsius"):
                result=(val-32)*5/9
            elif(p=="Celsius" and q=="Kelvin"):
                result=val+273.15
            elif(p=="Kelvin" and q=="Celsius"):
                result=val-273.15
            elif(p=="Fahrenheit" and q=="Kelvin"):
                result=((val-32)*5/9)+273.15
            elif(p=="Kelvin" and q=="Fahrenheit"):
                result=((val-273.15)*9/5)+32
            else:
                msg.showerror("Error","Invalid conversion.")
                return
            b.config(state="normal")
            b.delete(0,tk.END)
            b.insert(0,result)
            b.config(state="readonly")
        except(Exception):
            msg.showerror("Error","Enter a valid decimal number.")
    win=tk.Toplevel(root)
    win.title("Temperature")
    win.config(bg="#1e1e1e")
    win.geometry("300x400")
    win.resizable(False,False)
    tk.Label(win,text="Temperature",font=("Digital-7 Mono",20,"bold"),bg="#1e1e1e",fg="orange").pack(pady=15)
    cb2=ttk.Combobox(win,font=("Segoe UI",12,"bold"),value=["Celsius","Fahrenheit","Kelvin"],state="readonly",justify="center")
    cb2.pack(pady=5)
    cb2.current(0)
    a=tk.Entry(win,font=("Segoe UI",12,"bold"),justify="center")
    a.pack(pady=5)
    cb3=ttk.Combobox(win,font=("Segoe UI",12,"bold"),value=["Celsius","Fahrenheit","Kelvin"],state="readonly",justify="center")
    cb3.pack(pady=5)
    cb3.current(1)
    b=tk.Entry(win,font=("Segoe UI",12,"bold"),state="readonly",justify="center")
    b.pack(pady=5)
    tk.Button(win,text="Calculate",font=("Segoe UI",10,"bold"),bg="orange",fg="white",command=calc_temp).pack(pady=10)
   
root=tk.Tk()
root.title("Calculator")
root.config(bg="#2e2e2e")
root.geometry("360x550")
root.resizable(False,False)
md="default"

menubar=tk.Menu(root)

#View:
size=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=size)
size.add_command(label="Mini Mode",command=mini)
size.add_command(label="Default",command=norm)
size.add_separator()
size.add_command(label="Exit",command=out)

#Mode:
mbar=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Mode",menu=mbar)
mbar.add_command(label="BMI",command=bmi)
mbar.add_command(label="GST",command=gst)
mbar.add_command(label="Discount",command=discount)
mbar.add_command(label="Numeral System",command=num)
mbar.add_command(label="Temperature",command=temp)
mbar.add_separator()

#Help:
hbar=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=hbar)
hbar.add_command(label="Info",command=hlp)

root.config(menu=menubar)

#Frame:
frame1=tk.Frame(root,bg="#3b3b3b")
frame1.pack(fill="x",padx=10,pady=10)
frame2=tk.Frame(root,bg="#3b3b3b")
frame2.pack(expand=True,fill="both",padx=5,pady=5)

#Entry:
entry=tk.Entry(frame1,font=("Digital-7 Mono",32),bg="white",fg="black",borderwidth=0,relief="flat",justify="right",state="readonly")
entry.pack(fill="both",expand=True,padx=5,pady=5,ipady=10)

#Buttons
for i in range(4):  # 4 columns
    frame2.grid_columnconfigure(i, weight=1)
for i in range(5):  # 5 rows
    frame2.grid_rowconfigure(i, weight=1)

buttons = [["AC","C","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["00","0",".","="]]

colors = {"AC":"orange", "C":"orange", "%":"orange", "÷":"orange",
        "×":"orange","-":"orange","+":"orange","=":"orange",
        "0":"white","00":"white",".":"white",
        "1":"white","2":"white","3":"white",
        "4":"white","5":"white","6":"white",
        "7":"white","8":"white","9":"white"}

exp=""

def click(value):
    global exp
    if(value=="AC"):
        exp=""
    elif(value=="C"):
        exp=exp[:-1]
    elif(value=="="):
        try:
            exp=exp.replace("×","*")
            exp=exp.replace("÷","/")
            result=str(eval(exp))
            exp=result
        except:
            exp="Error"
    else:
        exp+=str(value)

    entry.config(state="normal")
    entry.delete(0,tk.END)
    entry.insert(tk.END,exp)
    entry.config(state="readonly")

for r in range(5):
    for c in range(4):
        text = buttons[r][c]
        b = tk.Button(frame2, text=text, bg="#636e72", fg=colors[text], font=("Arial",16,"bold"),command=lambda val=text:click(val))
        b.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

root.bind("<Key>", key_event)
root.mainloop()
