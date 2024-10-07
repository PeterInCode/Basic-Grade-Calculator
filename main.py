# A list lets me store multiple values in one place.

grades = []  # This is an empty list where I an storing the grades the user enters.

# I will ask the user how many grades they want to input, for that i am using input
num_grades = int(input("How many grades do you want to enter? "))

# Since i want to do the same logic multiple times, on the grades, loop "For" can help me

for i in range(num_grades):
    # Inside this loop, we ask for one grade at a time and add it to the list.
    grade = float(input(f"Enter grade #{i+1}: "))
    grades.append(grade)  # The append() function adds the grade to the list.

# Now we have all the grades, so we can calculate the average.
# To do this, we add up all the grades and divide by the number of grades.
# The sum() function adds up all the values in the list, and len() gives the total number of items in the list.

average_grade = sum(grades) / len(grades)
dds
# Next, we'll print out the average.
print(f"Your average grade is: {average_grade}")

# Based odsan the average, we can decide if the student has passed or failed.
# Let's assume that an average of 60 or more is a pass. dssa

if average_grade >= 50:
    print("Congratulations, you passed")dsfds
else:
    print("Sorry, you failed")ffds
