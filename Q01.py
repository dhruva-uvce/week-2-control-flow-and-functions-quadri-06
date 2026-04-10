# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
x = int(input("Enter your score: "))
if (x>=90 and x<=100):
    print("Grade: A")
elif (x>=80 and x<90):
    print("Grade: B")
elif (x>=70 and x<80):
    print("Grade: C")
elif (x>=60 and x<70):
    print("Grade: D")
elif (x<60):
    print("Grade: F")
