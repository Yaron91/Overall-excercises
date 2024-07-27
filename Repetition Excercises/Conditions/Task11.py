age: int = int (input ("Please enter your age: "));
height: int = int (input ("Please enter your height in centimeters: "));
if age >= 8 and age <= 18:
    if height > 115:
        print ("You may enter the rollercoaster")
    else:
        print (f" You are missing {(116 - height)} cm to enter")
elif age >18:
    if height > 100:
        print ("You may enter the rollercoaster")
    else:
        print (f" you are missing {(101 - height)} cm to enter")
else:
    print(f"You need to wait {(8 - age)} years before you enter");

