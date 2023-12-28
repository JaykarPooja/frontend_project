# list=[1, 5, 5, 6, 8, 7]
# print(list)
# print(list[0],list[5])
# print(list[0],list[-1]) # reverse indexing possible in python -1,-2,-3
# print(id(list[1]), id(list[0]),id(list[2]),id(list[3]))


# y=10
# print("adress of y= ", id(y),type(y))
# x=[10,1]
# print("adress of x= ", id(x[0]),type(x), type(x[0]))

# num1=10
# num2=10
# print("num1 = ", num1, "adress of num1", id(num1))
# print("num2 = ", num2, "adress of num2", id(num2))

# num1+=10
# print("num1 = ", num1, "adress of num1", id(num1))
# print("num2 = ", num2, "adress of num2", id(num2))


# list1 = [4,5,8]
# list2 = list1
# print(list1)
# print(list2)

# list1[1] = 10
# print(list1)
# print(list2)

# list2[1] = 5
# print(list1)
# print(list2)

# list1 = [4,5,8]
# list2 = list1.copy() # .copy just make a clone of list1
# print(list1)
# print(list2)

# list1[1] = 10
# print(list1)
# print(list2)

# list2[1] = 5
# print(list1)
# print(list2)


# list = ["Pooja","Nita"]
# print (list[0], list[1])
# list[0] = "rachna"
# print(list)

# nums = [11,12,13,14,15]
# nums[4]= 30    # forward indexing - 0,1,2,3,4
# print(nums)
# nums[-1]= 60   # reverse indexing - -1,-2,-3
# print(nums)

nums = [11,12,13,14,15]
num2=[1,2,3]
# print(nums)
# nums.append(24)
# print(nums)
# nums.append(40)
# print(nums)
# nums.append((2,3,4,5)) # but it will add as a list hence extend is used
# print(nums)

# nums = [11,12,13,14,15]
# print(nums)
# nums.insert(2,50)
# print(nums)

nums = [11,12,13,14,15]
# num2 = [20,30,40]
# print(nums)
# nums.extend(num2)
# print(nums)
# num3 = (1,2,3,4,5)
# nums.extend(num3)
# print(nums)
# ### or can write in below method also
# nums.extend([55,45,66])
# print(nums)




