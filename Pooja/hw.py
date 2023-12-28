#1 to take input from user. input always in string format needs to convert in int
""" 
Physics = int(input("Enter Physics marks - "))
Chemistry = int(input("Enter Chemistry marks - "))
Biology = int(input("Enter Biology marks - "))
Mathematics = int(input("Enter Mathematics marks - "))
Computer = int(input("Enter Computer marks - "))

Total = Physics + Chemistry + Biology + Mathematics + Computer
print("Toal of Marks of all sub ", Total )
per = Total/5
print("Percentage of all ", per, "%")

if per >= 90.0 :
    print("Student has got Grade A")
elif per >= 80.0 :
    print("Student has got Grade B")
elif per >= 70.0:
    print("Student has got Grade C")
elif per >= 60.0 :
    print("Student has got Grade D")
elif per >= 40.0 :
    print("Student has got Grade E")
elif per <= 40.0 :
    print("Student has got Grade F")
else:
     print("Please enter right marks"); """

#2 To check num is even or odd
""" num=int(input("Enter any no- "))
num = num % 2
if num == 0:
    print("Number is Even")
else:
    print("Number is Odd") """

#3 To find gross salary
""" BS = int(input("Enter Basic Salary "))

if BS <= 10000:
    HRA = BS * (20/100)
    DA  = BS * (80/100)
    GS  = BS + HRA + DA
    print(" Gross Salary is - ", GS)
elif BS <= 20000:
    HRA = BS * (25/100)
    DA  = BS * (90/100)
    GS  = BS + HRA + DA
    print(" Gross Salary is - ", GS)
elif BS > 20000:
    HRA = BS * (30/100)
    DA  = BS * (95/100)
    GS  = BS + HRA + DA
    print(" Gross Salary is - ", GS)
else:
    print("Please enter right amount") """

#4 to calculate profit and loss
""" costPrice = int(input("Enter cost price"))
sellingPrice = int(input("Enter selling price"))
 
if sellingPrice == costPrice :
    print("No profit nor Loss")
 
elif sellingPrice > costPrice :
    Profit = (sellingPrice - costPrice)
    print("Profit of ", Profit, "Rs" )
 
else :
    Loss = costPrice - sellingPrice
    print("Loss of ", Loss, "Rs") """







     

