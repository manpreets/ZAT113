
total = 0
count = 0
while True:
    user_input = input("Enter the number or write Done to end : \n")

    if user_input.lower() == "done":
        break
    else:
        try:
            total = total + int(user_input)
            count = count + 1
        except:
            print("Enter a number only")
            continue

print("Total : " + str(total))
print("Average : " + str(total / count))
print("Count : " + str(count))


