from tkinter import *;
root=Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")
#heading
Label(root,text="Python Registration Form",font="arial 15 bold").grid(row=0,column=3);
#feild name
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="Payment Mode")
#packing feilds
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#variable for storing data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmodevalue=StringVar
checkvalue=IntVar
#creating entry feild
nameentry=Entry(root,textvariable=namevalue) 
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
#packing entry feild
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#check box creating
checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)




root.mainloop()
