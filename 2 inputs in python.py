# input("Enter the name :")

# ............................................................


# name = input("enter the name:")
# print("Welcome",name)



# name = input("enter the age:")
# print("age is",name)

# ''''''''''''''''''''''''''''''''''''''''''''''''''


# a= input("enter the values:")
# print(type(a),a)

#     always in the output the ans is given in STRING data type.....
#   even if you take the values in INT or FLOAt The output is given in Srting only.....

# ..........................................

# a= int(input("enter the values:"))
# print(type(a),a)

#    and if you want the input to show the other Data type in thr output.....
#    we need to add the suitable data type beside the Iinput value which will give the output according to the input values

# a= float(input("enter the values:"))
# print(type(a),a)

# .............................................................


# name = input("enter the name: ")
# cell = input("enter the cell no.:")
# marks = input("Enter the marks:")

# print("Welcome:",name)
# print("enter cell no.:", cell)
# print("enter the marks", marks)

# ...... here the output is correct but it is Showing in the STring format....so we need to write in Standardadized form by
#     adding the data type before the inputs which stores in the datatype form rether than string format ..


# name = input("enter the name: ")
# cell = int(input("enter the cell no.:"))
# marks = float(input("Enter the marks:"))

# print("Welcome:",name)
# print("enter cell no.:", cell)
# print("enter the marks", marks)

# .........................................................................................................................

# Q1] Write a program to input 2 numbers and print their Sum ?
# a=int(input("value1:"))
# b=int(input("value2:"))

# print ("sum:", a+b)

# ........................................................................



# Q2]WAP to input side of a Square and print its area?

# Ans. Area of Square = A*A
# side = float(input ("enter size of side of the square:"))
# print("Area of the square:", side*side)
# you can even take integer or float which ever you want...
                    #   (or)
                        
# side = float(input ("enter size of side of the square:"))
# print("Area of the square:", side **2)

# ........................................................................


# Q3]WAP to input 2 floating point numbers and Print their Average
# a = float(input ("enter value1:"))
# b= float(input ("enter value2:"))
# print("Average value is :", (a+b)/2)

# or

# a = float(input ("enter value1:"))
# a= float(input ("enter value2:"))
# print("Average value is :", (a+a)/2)
#  we can give same variable names in python and it will take the values seperately without any errors....but
#  we need to assige different variable names to the calues which is helpful to read the code easily and it is the standard format

# ..................................................................................

# Q4]WAP to input 2 int numbers , a And b.
#    Print True if a is greater than or q=equal to b . if not print False.

# a= int(input("enter the value1:"))
# b= int(input("enter the value2:"))
# print(a>=b)


#           (or) By using if Else .......

# a= int(input("enter the value1:"))
# b= int(input("enter the value2:"))
# if(a>b):
#  print("True")
# else:
#  print("False")