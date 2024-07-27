sum = None
while True:
    x: int = int (input("Please enter a number. To stop please enter -99: "));
    if x == -99:
        break
    if sum == None:
        sum = 0
    sum = x + sum
print (f"The sum of all the numbers is {sum}");