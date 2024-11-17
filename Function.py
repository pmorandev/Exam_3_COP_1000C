# ##############################################################################
#  Written by: Evan McDaniel, Khalid Elmounaichet, and Pedro Moran             #
#  Date Written: 11-17-2024                                                    #
#  Purpose: The purpose of the following source code is to create a program    #
#  that execute a series of operations on a list of grades.                    #
# ##############################################################################

# Continuously prompts the user for grades and adds them to the grades list until the exit flag (-999) is entered.
def getScoresUntilExitFlag(grades: []):
    newGrade = -1
    while(newGrade != -999):
        newGrade = getOneGrade(grades, exitFlag=True)

# Prompts the user to enter a grade between 0 and 110. Returns -999 if the exit flag is set, otherwise returns the entered grade.
def getOneGrade(grades: [], exitFlag = False):
    newGrade = -1
    while(newGrade < 0 or newGrade > 110):
        try:
            newGrade = float(input("Please enter one grade between 0-110: "))
            if(exitFlag == True and newGrade == -999):
                return -999
        except:
            newGrade = -1
    grades.append(newGrade)
    return newGrade

# Removes all grades below 70 from the grades list and returns the filtered list.
def removeFGrades(grades:[]) -> []:
    return [grade for grade in grades if grade >= 70.0]

# Decreases each grade by 5, ensuring that no grade goes below 0. The grades list is modified in place.
def adjustGrades(grades:[]):
    for i in range(len(grades)):
        grades[i] = grades[i] - 5
        if(grades[i] < 0):
            grades[i] = 0