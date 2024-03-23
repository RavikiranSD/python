# #using function for performing thr tasks:
# def calc_sum(a,b):
#     sum=a+b
#     # print(sum)
#     return sum

# # print(calc_sum(5,6))
# calc_sum(5,7)
# calc_sum(5,8)
# calc_sum(5,9)

# #..................................................................
# #returning NONE value in output

# def print_hello():
#      print("hello")   
# output=print_hello()
# print(output)

# #.........................................................

# #Create a function to ccalculate average of 3 numbers

# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg

# calc_avg(98,97,95)
# calc_avg(47,52,83)

# #................................................................................
# #default parameters:

##ex:
# def calc_prod(a=1,b=1):
#     print(a*b)
#     return a*b

# calc_prod( )  #default value comes in o/p
# calc_prod(2,6)

##ex: 
# #you can add only 1 default parameters while function defining ,BUT it should be stsrt from the last 

# def calc_prod(a,b=1):
#     print(a*b)
#     return a*b

# calc_prod(5 )  #default value comes in o/p
# calc_prod(2,6)

# #ex:
# def calc_prod(a,b,c=2,d=3):
#     print(a*b*c*d)
#     return a*b*c*d

# calc_prod(1,1)
# calc_prod(2,3,4,5)


# #(
# #making a function to call in another finction
# # calc_avg(23,44,54)
# #def add(b,c):
#    # sum = b+c
#     # print(sum)
#    # return sum
# #print(add(5,6))
# # def aa(add):
# #     dd=add+d
# #     print(dd)
# #     return dd   
  
# # aa(7)
# #                                                   )


# #=============================================================================================================================

# #Q1)Write a Function to print the length of a list(list in the parameter)

# heros=["ben 10","wanda","black_panther","iron_man"]
# cities=["delhi","banglore","kalaburagi","yadgir","bidar","vijayapura"]

# def print_len(list):
#     print(len(list))
#     #print(list)

# print_len(cities) 


# #...............................................................................................................

# #Q2)WAF to print the elements of a list in a single line(list is the parameter)

# heros=["ben 10","wanda","black_panther","iron_man"]
# cities=["delhi","banglore","kalaburagi","yadgir","bidar","vijayapura"]

# def print_list(list):
#     for item in list:
#         # print(item)      #just by printing like this all the values comes prints line by line ........
#                           #and DO NOT print in a SINGLE LINE  so use the end=" "(ending of space)
        
#         print(item, end=",")  #you can use any symbol in the end space


# print_list(heros)    #calling function  

# #.............................................................................................................

# #Q3)WAF to find the factorial of n.(n is the parameter)

# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#         # print(fact)       #always give correct indentation to the code ...
#     print(fact)

# calc_fact(4)

# calc_fact(6)

#.........................................................................................

# #Q4)WAF to convert USD into INR.


# def convertor(usd_val):
#     inr_val = usd_val*83
#     print(usd_val,"usd=", inr_val, "INR")

# convertor(5)
# convertor(6)
# convertor(88)
# convertor(70)

# #....................................................................................................

# #usd_val=8   #(simple code )

# #inr_val =usd_val*80
# #print(inr_val)

