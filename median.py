<<<<<<< HEAD
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""




while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()

if (len(numbers) % 2 == 1):
    print(numbers[len(numbers) // 2])
else:
>>>>>>> 4acb48bac781421d489deb887f0d86c9cf69b5cc
    print(((numbers[len(numbers) // 2]) + (numbers[len(numbers) // 2 - 1])) / 2)
