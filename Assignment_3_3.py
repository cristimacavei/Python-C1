# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
s = float(score)
if s >= 1:
    print("The grade is too high")
elif s >= 0.9:
    print("Score is: A")
elif s >= 0.8:
    print("Score is: B")
elif s >= 0.7:
    print("Score is: C")
elif s >= 0.6:
    print("Score is: D")
elif s < 0.6:
    print("Score is F")
