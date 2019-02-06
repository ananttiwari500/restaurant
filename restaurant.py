from tkinter import*
import random
import time
#import datetime
import json
import csv

# just
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_resolution = str(screen_width)+'x'+str(screen_height)

root.geometry(screen_resolution)

#root.geometry("1200x800")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#TIMEm
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="HYDRANGEA RESTAURANT ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()
my_dict={}

# hello there

def Ref():
    x=random.randint(1,10000)
    randomRef=str(x)
    rand.set(randomRef)
    my_dict['Reference No.']=randomRef

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())
        my_dict['Fries']=CoFries


    
    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())
        my_dict['Noodles']=CoNoodles



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())
        my_dict['Soup']=CoSoup


    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())
        my_dict['Burger']=CoBurger

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())
        my_dict['Sandwich']=CoSandwich

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())
        my_dict['Drink']=CoD

                   
    CostofFries =CoFries * 70
    CostofDrinks=CoD * 60
    CostofNoodles = CoNoodles* 90
    CostofSoup = CoSoup * 80
    CostBurger = CoBurger* 100
    CostSandwich=CoSandwich * 90

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))
    my_dict['Cost of Meal']=CostofMeal

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.2)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)

    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)
    my_dict['Service Charges']=Service

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))
    my_dict['Total Cost']=OverAllCost

    PaidTax= "Rs", str ('%.2f' % PayTax)
    my_dict['Tax']=PaidTax

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")

# rand = StringVar()
# Fries=StringVar()
# Noodles=StringVar()
# Soup=StringVar()
# SubTotal=StringVar()
# Total=StringVar()
# Service_Charge=StringVar()
# Drinks=StringVar()
# Tax=StringVar()
# Cost=StringVar()
# Burger=StringVar()
# Sandwich=StringVar()
# my_dict={}

def qPrint():
    filename = "%s.csv" % my_dict['Reference No.']
    # fp = open(filename, 'w')
    # # fp.write(str(data))
    # fp.close

    # js = json.dumps(my_dict)
    # f = open(filename,"w")
    # f.write(js)
    # f.close()

    w = csv.writer(open(filename, "w"))
    for key, val in my_dict.items():
        w.writerow([key, val])

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="Fries",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=1)


lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)


btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

btnPrint=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Print",bg="powder blue",command=qPrint).grid(row=7,column=4)


root.mainloop()


#just chheking
