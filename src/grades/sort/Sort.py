# ##############################################################################
#  Written by: Evan McDaniel, Khalid Elmounaichet, and Pedro Moran             #
#  Date Written: 11-17-2024                                                    #
#  Purpose: The purpose of the following source code is to create a program    #
#  that execute a series of operations on a list of grades.                    #
# ##############################################################################

# Sorts the grades list in descending order (from highest to lowest).
def orderGradesFromHighToLow(grades:[]) -> []:
    return sorted(grades, reverse=True)

# Sorts the grades list in ascending order (from lowest to highest).
def orderGradesFromLowToHigh(grades:[]) -> []:
    return sorted(grades)

# Returns the highest, lowest, and average grade from the grades list.
# If the list is empty, returns default values (0, 0, 0).
def getGradeStats(grades:[]) -> (float, float, float):
    highest, lowest, average = (0, 0, 0)
    gradesLength = len(grades)
    if(gradesLength > 0):
        sortedGrades = orderGradesFromHighToLow(grades)
        lowest = sortedGrades[gradesLength - 1]
        highest = sortedGrades[0]
        average = __getAverageGrades__(grades)
    return (highest, lowest, average)

# Calculates and returns the average grade from the grades list.
def __getAverageGrades__(grades:[]) -> float:
    gradesLength = len(grades)
    totalGrades = 0.0
    for grade in grades:
        totalGrades = totalGrades + grade
    return totalGrades / gradesLength

# Returns the count of grades in each letter grade category (A, B, C, D, F) based on the grades list.
def getCountGrades(grades:[]) -> (int, int, int, int, int):
    aCounts, bCounts, cCounts, dCounts, fCounts = (0, 0, 0, 0, 0)
    for grade in grades:
        if 90 <= grade <= 110:
            aCounts = aCounts + 1
        elif 80 <= grade <90:
            bCounts = bCounts + 1
        elif 70 <= grade < 80:
            cCounts = cCounts + 1
        elif 60 <= grade < 70:
            dCounts = dCounts + 1
        else:
            fCounts = fCounts + 1
    return (aCounts, bCounts, cCounts, dCounts, fCounts)