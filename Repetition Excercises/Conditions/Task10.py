salary: int = int ( input("Please enter your monthly salary: "));
if salary > 50000:
    #0+600+1200+2100+4000+ 6750 = 14,650 which is the tax up to the point of earning 50,000
    current_tax: float = float (salary - 50000) * 0.51 + 14650
    print (f"The tax for the {salary} is {int (current_tax)}")
elif salary > 35000:
    #14650-6750 = 7,900
    current_tax: float = float (salary - 35000) * 0.45 + 7900
    print(f"The tax for the {salary} is {int(current_tax)}")
elif salary > 25000:
    #7900-4000 = 3900
    current_tax: float = float(salary - 25000) * 0.40 + 3900
    print(f"The tax for the {salary} is {int(current_tax)}")
elif salary > 18000:
    #3900 - 2100 = 1800
    current_tax: float = float(salary - 18000) * 0.30 + 1800
    print(f"The tax for the {salary} is {int(current_tax)}")
elif salary > 12000:
    #1800 - 1200 = 600
    current_tax: float = float(salary - 12000) * 0.20 + 600
    print(f"The tax for the {salary} is {int(current_tax)}")
elif salary > 6000:
    current_tax: float = float(salary - 6000) * 0.10
    print(f"The tax for the {salary} is {int(current_tax)}")
else:
    print(f"Your salary is {salary} which is not tax-required ")

