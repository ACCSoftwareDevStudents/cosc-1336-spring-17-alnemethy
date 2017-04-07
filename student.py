
class Student:
    
    def __init__(self, student_id, first_name, last_name, enroll_date):
        self.__student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.enroll_date = enroll_date
        

    def set_student_id(self, student_id):
        self.__student_id = student_id


    def get_student_id(self):
        return self.__student_id


