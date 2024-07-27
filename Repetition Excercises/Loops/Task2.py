number_1: int = int (input ("Please enter the first number: "));
number_2: int = int (input ("Please enter the second number: "));
if number_1 > number_2:
    for i in range (number_2 , number_1 + 1):
        print (i, end=',')
else:
    for i in range (number_1, number_2 +1):
        print (i, end=',')