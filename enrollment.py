from professor import Professor
from student import Student

class Enrollment:

    def __init__(self, enroll_id, student, course, grade, professor_id):

        self.enroll_id = enroll_id
        self.student = student 
        self.course = course
        self.grade = ''
        self.professor_id = professor_id
            
        

    def print_record(self):

        print(self.enroll_id,
              format(self.student.last_name, '15'),
              format(self.student.first_name, '15'),
              format(self.course.title, '20'),
              format(self.grade, '5'),
              format(self.professor.last_name ,'15'),
              format(self.professor.first_name, '5'))



