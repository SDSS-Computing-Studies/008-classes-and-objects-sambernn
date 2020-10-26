#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grades = []

    def __init__(self, name, studentNumber, grade): # You will need to create your own input parameters for all methods
        self.name = student(0)
        self.studentNumber = student(1)
        self.grade = student(2)

    def __del__():
        print("Deleted student info")

    def average(self):
        ave = sum(self.courses()) / len(self.courses())
        return ave

    def getHonorRoll(self, courses):
        honor = self.courses()
        honor.sort()
        honor.remove(-1,-2,-3)
        x = sum(honor) / len(honor)
        if x > 86
            return True
        else:
            return False
        


    def showCourses(self, courses):
        print(self.courses)

    def showGrade(self, x):
        x = input("Enter your course number:")
        self.courses[x]
        self.grades[x]
         

    def getCourses(self, courses):
        self.courses = courses

    def getGrades(self, grades)
        self.grades = grades
        



def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()