
num: int = int(input("Please enter a number. To exit enter a negative number or 0: "));
if num == -99:
    the_min = None
    the_max = None
else:
    the_max = num
    the_min = num

while True:
    if num == -99:
        break
    if num <= 0:
        break
    if num > the_max:
        the_max = num
    if num < the_min:
        the_min = num
    num: int = int(input("Please enter a number. To exit enter a negative number or 0: "));

print (the_max)
print (the_min)



