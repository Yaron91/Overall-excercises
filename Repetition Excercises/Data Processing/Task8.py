prime: int = int(input("Please enter a number: "));
if prime < 1:
    print(f"The number you chose,{prime}, is not a prime number.")
is_prime = True
for i in range (2, prime):
    if prime % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"The number you chose,{prime}, is a prime number.")
else:
    print(f"The number you chose,{prime}, is not a prime number.")