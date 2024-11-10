'''##############################################################################
## Written by......: khalid elmounaichet                                   ###
## Date Written....: Oct 17, 2024                                          ###
## Purpose.........: The last assignment. list, scores, chart              ###
##############################################################################'''

import random
def generate_random_grades(num_grades):
    """Generates a list of random grades between 0 and 110"""

    grades = []
    for _ in range(num_grades):
      grades.append(random.randint(0, 110))
    return grades

# Example usage:
grades = generate_random_grades(10)
print(grades)
####################################################################################
def display_grades(grades):
    """Display a list of grades between 0 and 100
    Args:
    grades: A list of numerical grades.
    """
    for grade in grades:
        if 0 <= grade <= 110:
            print(grades)
        else:
            print("Invalid grade:", grade)
# Example usage:
grades = [60, 70, 80, 90, 110]
display_grades(grades)
######################################################################################
def counts_grade_letters(grades):
    """Counts the occurrences of each grade letter in a list of grades.
    Args:
        grades (list): A list of numerical grades.
    Returns:
        dict: A dictionary where keys are grade letters and values are their counts.
    """
    grade_counts = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0
    }
    for grade in grades:
        if 90 <= grade <= 110:
            grade_counts['A'] += 1
        elif 80 <= grade <90:
            grade_counts['B'] += 1
        elif 70 <= grade < 80:
            grade_counts['C'] += 1
        elif 60 <= grade < 70:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1

    return grade_counts
def display_grade_counts(grade_counts):
    """Display the grade counts in a formatted way.
    Args:
        grade_counts (dict): A dictionary of grade letters and their counts.
    """
    for grade, count in grade_counts.items():
        print(f"{grade}: {count}")

if __name__=="__main__":
    grades = [110, 85, 95, 78, 88,65, 45]
    counts = counts_grade_letters(grades)
    display_grade_counts(counts)




###########################################################################################
def grade_chart(grade):
    """Prints a grade chart using 'x' characters."""
    if 0 <= grade <= 100:
        num_x = int(grade / 10)   # calculate the number of 'x's
        print(f"Grade: {grade} {'x' * num_x}")
    else:
        print("Invalid grade. Please enter a grade between 0 and 110. ")
# Example usage:
grade_chart(50)
grade_chart(65)
grade_chart(75)
grade_chart(80)
grade_chart(90)
grade_chart(100)
grade_chart(110)
###########################################################################################
def remove_below_70(grades):
    """Removes all grades below 60 from a list.
    Args:
        grades: A list of numerical grades.
    Returns:
    """
    return [grade for grade in grades if grade >= 70]

# Example usage
grades = [ 100, 80, 65,60,90, 110]
filtered_grades = remove_below_70(grades)
print(filtered_grades) # Output: [85, 75, 80, 90]
##############################################################################################
def adjust_grade(scores):
    """Adjusts the grade score by 5 points."""
    return score + 5

# Example usage
score = 75
adjust_score = adjust_grade(score)
print("Original score:", score)
print("Adjusted score:", adjust_score)
####################################################################################################
def score_stats(grades):
    """
    Calculate and displays the highest, lowest, and the average score from a list of grades.
    Args:
        grades: A list of numerical grades.
    """

    if not grades:
        print("No grades provided.")
        return
    highest = max(grades)
    lowest = min(grades)
    average = sum(grades) / len(grades)
    print(f"Highest grade:, {highest}")
    print(f"Lowest grade:, {lowest}")
    print(f"Average score: {average}")

# Example usage
score = [60, 75, 85, 95, 100, 110]
score_stats(grades)
#####################################################################################################
def display_scores_ascending(scores):
    """Displays the given scores in ascending order."""
    scores.sort()    # Sort the scores in-place
    print("Exam Scores (lowest to highest):", scores)

if __name__ =="__main__":
    scores =[]

    n = int(input("Enter an exam of scores: "))
    for i in range(n):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)
        display_scores_ascending(scores)






















