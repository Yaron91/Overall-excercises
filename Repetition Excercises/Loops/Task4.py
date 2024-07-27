max: int = int (input ("Please enter the first number: "));
den: int = int (input ("Please enter the second number: "));
for i in range (1, max + 1):
    if i % den == 0:
        print ( i, end=',')
