# Enter the value.
print("Check if input is a prime number")

try:
    n = int(input("Enter a positive number: \n"))

    is_prime = True

    if n == 0 or n == 1:
        is_prime = False

    i = 1

    while i <= n / 2:
        i = i + 1

        if n % i == 0:
            is_prime = False
            break

    print("Is " + str(n) + " prime - " + str(is_prime))
except:
    print("Program ended due to an error.")
