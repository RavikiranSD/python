# #ex:
# def function(n):
#     if(n==0):
#         return
#     print(n)
#     function(n-1)


# function(5)   #calling the function



# #ex:
# def show(n):
#     if(n<=-3):
#         return
#     print(n)
#     show(n-1)

# show(6)       #calling function


# #ex:recursion in factorial

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else: 
#         return fact(n-1)*n

# print(fact(5))


# #....................................................................................

# #write a recursive function to calculate the sum of first n natural numbers

# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n
    

# calc_sum(7)

# #Q2)write a recursive function to print all elements in a list.
# #    hint:use list & index as parameters.

# def print_list(list,idx=0):
#     if(idx== len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits=["banana","apple","litchi","mango"] 


# print_list(fruits)     #calling 