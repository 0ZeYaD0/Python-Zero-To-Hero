# 1 variabels (int,double,boolean)
#ex

first_name:str = "Zeyad"
age:int = 20
hight:float = 176.5
in_uni:bool = True

# 2 pritning and taking inputs
#the print func in py always print a new line in the end

print("What you want")

#the end will have what you put between the ''
print("etc",end=' * ')

# taking input from user in py the input func take the input as string

name:str = input()
print(name)

#if you want to take other inputs and use them you will have to use type casting

# 3 type casting
# if you want to use the input in like age in a func but you can't you will have to convert it from string to int

age:int = int(input())
hight:float = float(input())

#so now you know how to print and take inputs i will show an example for a small proram that takes the input from the user and print it

User_name:str = input()
User_age:int = int(input())
User_hight:float = float(input())

print(f"welcome {User_name} your age is {User_age} your hight is {User_hight}")


# 4 baisc math

# + for addition
# - for subtraction
# * for multblication
# / for division
# ** for power
# // for sqrt
# % used to check for the float point
# the = is for asginig a value to a variable and == to check if 2 things are the same
# here is small exaple of usage for all of them


User_age += 10
print(User_age)
User_age -= 10
print(User_age)
User_age *= 2
print(User_age)
User_age /= 2
print(User_age)
User_age **= 2
print(User_age)
User_age //= 2
print(User_age)


# 5 conditions (if, else, elif,match case)

if (User_age > 10):
    pass
elif(User_hight > 170):
    print("you are mid")
else:
    print("What the hell")

match User_age:

    case 10:
        print("You are young")
    
    case 20:
        print("You are mid")

# 6 basic logic (and,or)
# and return true if things you check for are all true so the put output will be true
# or return true when 1 of the things you are comparing is ture

num1 = 12
num2 = 11

if num1 == 12 and num2 == 11:
    pass
    # output is true so it will enter this condition if any of them not true it will not

if num1 == 12 and num2==10:
    pass
    #output is true since the first one is true so it will enter this condition


#now that we know how to check for spacfications and do math ill show a small program for a calculator

num_1:float = float(input())
num_2:float = float(input())
opration:str = input("Enter the opration [+, -, *, /, **, //]")

match opration:
    case '+':
        print(num_1 + num_2)

    case '-':
        if num_1 > num_2:
            print(num_1 - num_2)
        else:
            print(num_2 - num_1)

    case '*':
        print(num_1 * num_2)

    case '/':
        if num_2 == 0:
            print("Can't divide by Zero")
        else:
            print(num_1 / num_2)

    case '**':
        print(num_1 ** num_2)
    
    case '//':
        print(num_1 // num_2)

