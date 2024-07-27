num_1: int = int (input("Please enter the first number: "));
num_2: int = int (input("Please enter the second number: "));
if num_1 > num_2:
    for i in range (1 , num_2 + 1):
        if num_1 % i == 0 and num_2 % i == 0 :
            max_divide = i
else:
    for i in range (1 , num_1 + 1):
        if num_1 % i == 0 and num_2 % i == 0 :
            max_divide = i

print (f"The maximum number divided by {num_1} and {num_2} is {max_divide}")
