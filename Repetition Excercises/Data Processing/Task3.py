numbers = []
for i in range (5):
    number: float = float (input ("Please enter a number: "));
    numbers.append(number)
max_index:int = numbers.index(max(numbers))
print (f"The index of the highest number inserted is {max_index + 1}")