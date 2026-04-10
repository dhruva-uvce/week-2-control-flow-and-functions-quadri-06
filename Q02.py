# Q02. Leap Year Checker (if-else)
#
# Ask the user for a year (integer).
# Print whether it is a leap year or not.
#
# Rules:
#   - Divisible by 4 → leap year
#   - BUT divisible by 100 → NOT a leap year
#   - UNLESS also divisible by 400 → leap year
#
# Sample Input 1:   Enter a year: 2024
# Sample Output 1:  2024 is a leap year
#
# Sample Input 2:   Enter a year: 1900
# Sample Output 2:  1900 is not a leap year

# --- YOUR CODE HERE ---
x = int(input("enter a lead year: "))
if (x%4==0 and x%100!=0 or x%400==0):
    print(f"{x} is a lead year")
else:
    print(f"{x} is not a lead year")
