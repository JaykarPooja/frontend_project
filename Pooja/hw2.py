# for i in range (1,5):
#     for j in range (1,5):
#         print("*", end= " ") 
#     print()

# for i in range (1,5):
#     for j in range (1,5):
#         if i==1 and j==2 or i==1 and j==3 or i==1 and j==4 or i==2 and j==3 or i==2 and j==4 or i==3 and j==4:
#             print(" ", end= " ")
#         else:
#             print("*", end= " ") 
#     print()
    

# for i in range (1,5):
#     for j in range (1,5):
#         if i==2 and j==4 or i==3 and j==3 or i==3 and j==4 or i==4 and j==2 or i==4 and j==3 or i==4 and j==4:
#             print(" ", end= " ")
#         else:
#             print("*", end= " ") 
#     print()


# for i in range (1,8):
#     for j in range (1,5):
#         if i==1 and j==2 or i==1 and j==3 or i==1 and j==4 or i==2 and j==3 or i==2 and j==4 or i==3 and j==4 or i==5 and j==4 or i==6 and j==3 or i==6 and j==4 or i==7 and j==2 or i==7 and j==3 or i==7 and j==4:
#             print(" ", end= " ")
#         else:
#             print("*", end= " ") 
#     print()


# for i in range (1,5):
#     for j in range (1,5):
#         if i==1 and j==2 or i==1 and j==3 or i==1 and j==4 or i==2 and j==3 or i==2 and j==4 or i==3 and j==4 or i==3 and j==2 :
#             print(" ", end= " ")
#         else:
#             print("*", end= " ") 
#     print()


# Print number is a prime or not
# num = int(input("Enter a number: "))
# flag = False
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break;
#     if flag == True:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")

# for i in range (5):
#     for j in range (i+1,0,-1):
#         print(i, end=" ")
#     print()

lines = 5
for rows in range(lines):
    for space in range(lines-rows-1):
        print(" ", end=" ")
    for cols in range(rows + 1):
        print("*", end=" ")
    print()



