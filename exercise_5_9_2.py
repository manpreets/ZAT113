minimum = 0
maximum = 0
count = 0
while True:
    user_input = input("Enter the number or write Done to end : \n")

    if user_input.lower() == "done":
        break
    else:
        try:
            user_input_int = int(user_input)

            if count == 0:
                maximum = user_input_int
                minimum = user_input_int

            if user_input_int > maximum:
                maximum = user_input_int

            if user_input_int <= minimum:
                minimum = user_input_int

            count = count + 1
        except:
            print("Enter a number only")
            continue

print("Count : " + str(count))
print("Maximum : " + str(maximum))
print("Minimum : " + str(minimum))


