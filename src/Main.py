# ##############################################################################
#  Written by: Evan McDaniel, Khalid Elmounaichet, and Pedro Moran             #
#  Date Written: 11-17-2024                                                    #
#  Purpose: The purpose of the following source code is to create a program    #
#  that execute a series of operations on a list of grades.                    #
# ##############################################################################

from grades.sort import Sort
from grades.function import Function

# Main function responsible for holding the main flow of the program
def main():
    grades = []
    option = -1
    runProgramUntilGetExitFlag(option, grades)
    print("Good Bye!")

# Runs the main program loop, displaying the menu and processing user input until the exit flag is set (option 7).
def runProgramUntilGetExitFlag(option, grades: []):
    while (True):
        displayMainMenu()
        option = getOneValidOption()
        if(option == 7):
            break
        grades = performMenuOption(option, grades)

# Handles the user's menu choice and updates the grades list based on the selected option.
def performMenuOption(option: int, grades: []) -> []:
    if(option == 1):
        Function.getOneGrade(grades)
    elif(option == 2):
        Function.getScoresUntilExitFlag(grades)
    elif(option == 3):
        if(displayDisplayScoresMenu() == "a"):
            grades = Sort.orderGradesFromHighToLow(grades)
        else:
            grades = Sort.orderGradesFromLowToHigh(grades)
        displayGrades(grades)
    elif(option == 4):
        stats = Sort.getGradeStats(grades)
        counts = Sort.getCountGrades(grades)
        displayGradeStats(*stats)
        displayGradeCounts(*counts)
    elif(option == 5):
        Function.adjustGrades(grades)
    else:
        grades = Function.removeFGrades(grades)
        displayGrades(grades)
    return grades

# Displays the main menu options for the user to choose from.
def displayMainMenu():
    header = "|" + "*"*15 + "MAIN" + "*"*5 + "MENU" + "*"*15 + "|"
    print(header)
    print("1. Get One Exam Score")
    print("2. Get exam score until the user enters -999")
    print("3. Display All Exam Scores Entered")
    print("4. Display Exam Statistics")
    print("5. Adjust all Exam Statistics")
    print("6. Remove all F grades from the list")
    print("7. Quit the Program")
    print("|" + "*"*43 + "|")

# Displays options for sorting the grades and returns the user's choice.
def displayDisplayScoresMenu():
    validOption = "c"
    while(validOption not in ["a","b"]):
        print("a. From Highest to Lowest")
        print("b. From Lowest to Highest")
        validOption = input("Please choose one of the options above: ")
    return validOption

# Prompts the user for a valid menu option (1-7) and ensures the input is correct.
def getOneValidOption() -> int:
    option = 0
    while(option == 0):
        try:
            option = int(input("Please choose one of the options above: "))
            if(option not in [1,2,3,4,5,6,7]):
                option = 0
        except:
            option =  0
    return option

# Displays the grades list with letter grade labels (A, B, C, D, F) based on the score ranges.
def displayGrades(grades: []):
    print("|" + "*" * 15 + "GRADES" + "*" * 15 + "|")
    for grade in grades:
        if 90 <= grade <= 110:
            print(f"{grade:6.2f} -> A")
        elif 80 <= grade <90:
            print(f"{grade:6.2f} -> B")
        elif 70 <= grade < 80:
            print(f"{grade:6.2f} -> C")
        elif 60 <= grade < 70:
            print(f"{grade:6.2f} -> D")
        else:
            print(f"{grade:6.2f} -> F")
    print("|" + "*" * 15 + "GRADES" + "*" * 15 + "|")

# Displays the highest, lowest, and average grades as part of the grade statistics.
def displayGradeStats(highest, lowest, average):
    print("|" + "*"*15 + "GRADE STATS" + "*"*15 + "|")
    print(f"{'Highest':10}: {highest:.2f}")
    print(f"{'Lowest':10}: {lowest:.2f}")
    print(f"{'Average':10}: {average:.2f}")
    print("|" + "*" * 15 + "GRADE STATS" + "*" * 15 + "|")

# Displays the count of each grade category (A, B, C, D, F) from the grade list.
def displayGradeCounts(aCounts, bCounts, cCounts, dCounts, fCounts):
    print("|" + "*"*15 + "GRADE COUNTS" + "*"*15 + "|")
    print(f"{'As':10}: {aCounts:,}")
    print(f"{'Bs':10}: {bCounts:,}")
    print(f"{'Cs':10}: {cCounts:,}")
    print(f"{'Ds':10}: {dCounts:,}")
    print(f"{'Fs':10}: {fCounts:,}")
    print("|" + "*" * 15 + "GRADE COUNTS" + "*" * 15 + "|")

# Call to the main function
main()