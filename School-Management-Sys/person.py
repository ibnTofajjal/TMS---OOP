import random
from school import School

class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def evaluate_exam(self):
        return random.randint(1, 100)
    

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self._it = None
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
    
    def final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            sum += School.Person.grade_to_value(grade)
        gpa = sum / len(self.subject_grade)
        self.grade = School.Person.value_to_grade(gpa)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value