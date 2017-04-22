from course import Course
from student import Student
from enrollment import Enrollment
from professor import Professor
from transcript import Transcript
from school_initializer import SchoolInitializer
from school_db import SchoolDB

class Gradebook:


    def __init__(self, school_db):
        self.school_db = school_db
        self.enrollments = school_db.enrollments


    def main(self):

        choice = ''
        c = Course() ## ??

        while choice != 'e':

            choice = self.__main_menu()

            if choice == '1':

                enroll_key = int(input("Enter enroll key"))

                if enroll_key in self.enrollments:
                    enroll = self.enrollments.get(enroll_key)
                    c.trananscript(enrollment)   ###
                    

                    grade = input("Enter grade: ")
                    enroll.grade = grade

                else:
                    print("Key doesn't exist")

            elif choice == '2':

                student_id = int(input("Enter student id: "))

                if student_id in self.students:

                    student = self.students.get(student_id)
                    transcript = Transcript(self.enrollments)
                    transcript.print_transcript(student)

                else:
                    print("Student does not exist")

            elif choice == '3':

                for enrollment in self.enrollments.values():
                    enrollment.print_record()

            elif choice == '4':

                self.school_db.save_data()

    def __main_menu(self):

        print()
        print("Academic Menu")
        print()
        print("1) Update Grade")
        print("2) Print Student GPA")
        print("3) Print All Enrollments")
        print("4) Save Enrollments")
        print()

        return input("Enter 1,2,3 or 4.  e to exit: ")
    

school_db = SchoolDB(SchoolInitializer())
gradebook = Gradebook(school_db)
gradebook.main()
