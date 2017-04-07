

class Course:

    def __init__(self, course_id, course_name, course_credit_hours):
        self.__course_id = course_id
        self.course_name = course_name
        self.course_credit_hours = course_credit_hours

        
    def set_course_id(self, course_id):
        self.__course_id = course_id


    def get_course_id(self):
        return self.__course_id

        
