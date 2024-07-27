number_1: int= int (input ("Please enter the first number: "));
number_2: int= int (input ("Please enter the second number: "));
number_3: int= int (input ("Please enter the third number: "));
if number_1 > number_2 and number_1 > number_3:
    print ("The biggest number is ", number_1)
elif number_2 > number_3 and number_2 > number_1:
    print("The biggest number is ", number_2)
else:
    print("The biggest number is ", number_3)