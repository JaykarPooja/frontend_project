#for loop with range function
#range(starts,end, step)
#range(end) it will take default value for start= 0, and step=1
#range(starts,end)default value for step=1

# for i in range(1,11):
#     print(i)
# for i in range(10,0,-1):
#     print(i)

# fact of no.using while loop  
# i = 1
# fact = 1
# while(i <= 5):
#     fact = fact * i
#     i = i + 1
# print(fact)

# fact of no.using for in range loop  
# start = 1
# end = int(input("enter any num"))
# fact = 1
# for i in range(start,end+1):
#     fact = fact * i
# print(fact)

# even no.
# start = 1
# end = int(input("enter any num"))
# for i in range(start,end+1):
#     if i % 2 == 0 :
#         print(i)

# skip if i=3 and break the loop if i=6
# start = 1
# end = int(input("enter any num"))
# for i in range(start, end+1):
#     if i == 3:
#         continue
#     print(i)
#     if i == 6:
#         break

# find prime no.
#pattern printing
# for i in range(1,6):
#     for j in range(1,6):
#      print("*", end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#      print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(5,0,-1):
#      print(j, end=" ")
#     print()


# for i in range(1,4):
#     for j in range(1,4):
#      if i == 2 and j == 2:
#         print("o", end=" ")
#      else:
#         print("*", end=" ")
#     print()

for i in range(1,4):
    for j in range(1,4):
    #  if i == 1 and j == 1 or i == 3 and j == 3 or i == 1 and j == 3 or i == 3 and j == 1:
     if i%2 != 0 and j%2 != 0 :
        print("o", end=" ")
     else:
        print("*", end=" ")
    print()


    
