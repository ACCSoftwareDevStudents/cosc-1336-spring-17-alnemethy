from student import Student
from course import Course

class Enrollment:

    def __init__(self):
        self.grade_update_list = []

    def print_update_list(self, grade_update_list):

        for p in grade_update_list:
            print(p.course, p.student)


        print("Enroll ID", "Student Name", "Course Name", "Credit Hours", "Grade")
        print(self.grade_update_list)
                            

