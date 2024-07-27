number: int = int (input ("Please enter a 2- digits number: "));
if number > 99 or number < 10 :
    print ("Please re-try and enter a valid number!");
else:
    num_1 : int = number // 10
    num_2 : int = number % 10
    print ("The sum of the two numbers are",(num_1 + num_2))