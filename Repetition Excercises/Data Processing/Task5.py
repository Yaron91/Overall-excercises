num_1: int = int (input("Please enter the first number: "));
num_2: int = int (input("This number will be the power number: "));
power_num = 1
for i in range (num_2):
    power_num *= num_1

print(f"{num_1} in the power of {num_2} is {power_num}")
