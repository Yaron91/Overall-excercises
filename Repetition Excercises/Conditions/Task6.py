number: int = int (input ("Please enter a 4- digits number: "));
if number > 9999 or number < 1000 :
    print ("Please re-try and enter a valid number!");
else:
    second_right_number: int = (number // 10) % 10
    print (f"The digit on the right of {number} is {second_right_number}")