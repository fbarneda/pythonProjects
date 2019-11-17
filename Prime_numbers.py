"""
Find if the first 10 numbers are Prime numbers
"""

# Create a loop from 2 until 11 -- 1 is divisible by itself
# Check if each number is divisible by all numbers below itself, minus 1
# If it divisible - it's not prime
# If it is not divisible - so only the number 1 and itself can be used - then it's prime

for n in range(2, 11):
    for d in range(2, n):
        if n % d == 0:
            print(f"\t{n} is divisible by {d}")
            break
    else:
        print(f"{n} is prime")
