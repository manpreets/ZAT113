input = input("Enter temp in Celsius \n")
try:
    celsius = float(input)
     fahernheit = (celsius * 9 / 5) + 32
    print("Fahernheit : " + str(fahernheit))
except:
    print("Please enter a number")




