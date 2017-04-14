

class Transcript:

    def __init__(self, enrollments):

        self.enrollments = enrollments


    def print_transcript(self, student):

        print("Student: ",student.first_name + "" + student.last.name)
        sum_credit_hours = 0
        sum_grade_points = 0

        print("Course:              ")
        
        for e in self.enrollments.values():
            if e.student.student_id == student.student_id:

                if e.grade in ["A", "B", "C", "D", "F"]:
                    sum_credit_hours += e.course.credit_hours
                    
                sum_credit_hours += e.course.credit_hours
                grade_points = e.course.credit_hours * self.__get_credit_points(e.grade)

                sum_grade_points += grade_points

                print(format(e.course.title, '12'),
                      format(e.course.credit_hours, '13'),
                      format(credit_points, '12'),
                      format(grade_points, '12'),
                      format("  " + e.grade, '12'))

        print(format(sum_credit_hours, '26'),
              format(sum_grade_points, '26'))

        if sum_credit_hours > 0:
            print("GPA: ", format(sum_grade_points / sum_credit_hours, '.2f'))
                

        def __get_credit_points(self, letter_grade):

            credit_points = 0

            if letter_grade == "A":
                credit_points = 4
            elif letter_grade == "B":
                credit_points = 3
            elif letter_grade == "C":
                credit_points = 2
            else:
                letter_grade == "D"
                credit_points = 1


            return self.grade_point
            
            

