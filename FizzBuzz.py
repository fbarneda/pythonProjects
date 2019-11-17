"""
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".
"""

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz\t since {num} is a multiple of BOTH 3 and 5")
    elif num % 3 == 0:
        print(f"Fizz\t since {num} is a multiple of 3")
    elif num % 5 == 0:
        print(f"Buzz\t since {num} is a multiple of 5")
    else:
        print(num)