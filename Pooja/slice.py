# +++++++++++++++++++++++++++++++ slice ++++++++++++++++++++++++++
# str="ITVedant"
# sub=str[2:]
# print(sub)


# list1=[11,12,13,14,15]
# list2 = list1[2:]
# print(list2)

# list1.append(16)
# print(list1)
# list2 = list1[2:]
# print(list2)


# list2=list1[-2:-5:-1]
# print(list2)

# list2=list1[-2:-5]    # step=1
# print(list2)

# list2=list1[::-1]
# print(list2)


# ++++++++++++++++++++++++++++ in & not in operator +++++++++++++++++++
# num=[3,4,5,6,7]
# print(5 in num)
# print(5 not in num)



L1=[1,2,3]
L2=[4,5,6]
# L3=L1+L2
# print(L3)

# L1.append(10)
L3=L1+L2
L1.append(10)
print(L3)
L3.append(10)
print(L3)

num1=10
num2=0
sum=num1+num2
print(id(num1), id(sum))


