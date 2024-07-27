temp_list=[]
sum= 0
for i in range(12):
    while True:
        try:
            temp: float = float(input("Please enter the average monthly temperature in Tel- Aviv: "));
            if  -5 <= temp <= 40:
                print (f"Month {i + 1}: The temperature is {temp} degrees");
                temp_list.append(temp)
                sum += temp
                break
            else:
                print("Please enter a valid temperature between -5 and 40 degrees")
        except:
            print ("Please enter a number");
print (f"The average yearly temperature is {sum / len(temp_list):.2f} degrees");
print (f"The maximum temperature is {max(temp_list)}");
print (f"The minimum temperature is {min(temp_list)}")