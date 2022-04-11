user_input = input("Enter the score:|n")
try:
    score = float(user_input)
    if score >= 0.9:
        print("A")
    elif score >= 0.80:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("Please enter the score")
