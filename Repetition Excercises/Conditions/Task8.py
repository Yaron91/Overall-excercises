number: int = int (input ("Please enter a 2- digits number: "));
if number > 99 or number < 10 :
    print ("Please re-try and enter a valid number!");
else:
    num_1 : int = number // 10
    num_2 : int = number % 10
    print (f"The reverse number is {num_2}{num_1}")