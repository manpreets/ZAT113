n = 0
while True:
    n = n + 1
    print(n)

    if n % 3 == 1:
        print("     " + str(n) + " is a NOT special number! because " + str(n % 3))
        if n > 20:
            break
    else:
        print("     " + str(n) + " is a special number! because " + str(n % 3))


