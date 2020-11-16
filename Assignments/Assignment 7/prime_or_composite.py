def prime_or_composite(number):

    pass

if __name__ == "__main__":
    numbers = 7
if numbers > 1:
    for i in range (2, numbers):
        if (numbers % 1) == 0:
            print("It is not a prime number")
    else: 
        print("Is a prime number")
else:
    print("Is not a prime number")
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # Optional: If you want to test the efficency of your algorithm add this number to the array above -7
    # Optional: If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)