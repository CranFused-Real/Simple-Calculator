# Importing Modules

from time import sleep

# Welcome

print("Hello User!")
sleep (.2)
user_name = input("Please enter your name: ")
sleep (.2)
print("Your name is: ", user_name)
sleep (.2)


# Main Code

print("Please select from one of the following operations: ")
sleep (.2)
print("1 = Addition")
sleep (.2)
print("2 = Subtraction")
sleep (.2)
print("3 = Multiplication")
sleep (.2)
print("4 = Division")
sleep (.2)

# Getting user's input
user_input_1 = int(input("Enter number 1/2/3/4: "))
sleep (.2)

# If user selected Addition
if user_input_1 == 1:
    print("You have selected Addition")
    sleep (.2)
    print("Now you have to enter any two number which you have to Add")
    sleep (.2)
    add1 = int(input("> "))
    print("You entered: ", add1)
    sleep (.2)
    add2 = int(input("> "))
    print("You entered: ", add2)

    sum = add1 + add2
    sleep (.2)
    print(add1, "+", add2, "=", sum)
    sleep (.2)

    # Bye
    print("Thanks for using this Calculator programme!")
    sleep (.2)
    print("Hope you have a nice day!")
    sleep (.5)
    exit() # Exiting Programme

# If selected Subtraction
elif user_input_1 == 2:
    print("You have selected Subtraction")
    sleep (.2)
    print("Now you have to enter any two number which you have to Subtract")
    sleep (.2)

    sub1 = int(input("> "))
    print("You entered: ", sub1)
    sleep (.2)
    sub2 = int(input("> "))
    print("You entered: ", sub2)

    sub_ans = sub1 - sub2
    sleep (.2)
    print(sub1, "-", sub2, "=", sub_ans)
    sleep (.2)
    
    # Bye
    print("Thanks for using this Calculator programme!")
    sleep (.2)
    print("Hope you have a nice day!")
    sleep (.5)
    exit() # Exiting Programme

# If selected Multiplication
elif user_input_1 == 3:
    print("You have selected Multiplication")
    sleep (.2)
    print("Now you have to enter any two number which you have to Multiply")
    sleep (.2)

    mul1 = int(input("> "))
    print("You entered: ", mul1)
    sleep (.2)
    mul2 = int(input("> "))
    print("You entered: ", mul2)

    mul_ans = mul1 * mul2
    sleep (.2)
    print(mul1, "*", mul2, "=", mul_ans)
    sleep (.2)
    
    # Bye
    print("Thanks for using this Calculator programme!")
    sleep (.2)
    print("Hope you have a nice day!")
    sleep (.5)
    exit() # Exiting Programme

# If selected Division
elif user_input_1 == 4:
    print("You have selected Division")
    sleep (.2)
    print("Now you have to enter any two number which you have to Divide")
    sleep (.2)

    div1 = int(input("> "))
    print("You entered: ", div1)
    sleep (.2)
    div2 = int(input("> "))
    print("You entered: ", div2)

    div_ans = div1 / div2
    sleep (.2)
    print(div1, "/", div2, "=", div_ans)
    sleep (.2)
    
    # Bye
    print("Thanks for using this Calculator programme!")
    sleep (.2)
    print("Hope you have a nice day!")
    sleep (.5)
    exit() # Exiting Programme

else:
    print("Wrong Input!")
    sleep (.2)
    print("Exiting!")
    sleep (.2)
    sleep (.2)
    sleep (.2)
    exit()