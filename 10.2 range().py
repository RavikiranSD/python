# print(range(5))
# #o/p: range(0, 5)

# seq=range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# #O/P:
# # 0
# # 1
# # 2
# # 3
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# #using for loop:
# seq=range(10)
# for i in seq:
#     print(i)

#           #(OR)
# #the below method is mostly used in coding
# for i in range(10):
#     print(i)

# using the start,stop and step in range

# for i in range(10):  #range(stop)
#   print(i)

# for i in range(2,10):  #range(start,stop)
#   print(i)

# for i in range(2,10,3):  #range(start,stop,step)
#   print(i)

# #for printing even numbers:
# for i in range(1,20,2):
#     print(i)

# #for printing odd numbers:
# for i in range(1,20,2):
#     print(i)


# #solve questionf using for and range()

# #Q1)print number from 1to 100

# for i in range(1,101):
#     print(i)

# #Q2)print number from 100 to 1

# for i in range(100,0,-1):  #range(start,stop,step)
#     print(i)

# #Q3)print the multiplication table of a number n
# n=int(input("enter the number:"))

# for i in range(1,11):  #range(start,stop)
#     print(n * i)       #here the assigned integer(n) multiplies with the number from the range

#(or)
    
# n=4
# for i in range(1,11):  #range(start,stop)
#     print(n * i) 

