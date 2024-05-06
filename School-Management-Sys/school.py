class Shcool:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classroom = {}

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    
    def add_classroom(self, classroom):
        self.classroom[classroom.name] = classroom

    def students(self):
        pass

    @staticmethod 
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return "A+"
        elif marks >= 70 and marks < 80:
            return "A"
        elif marks >= 60 and marks < 70:
            return "B"
        elif marks >= 50 and marks < 60:
            return "C"
        elif marks >= 33 and marks < 50:
            return "D"
        else:
            return "F"
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }

        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value >=4.5 and value<=5.00:
            return 'A+'
        elif value >= 3.5 and value <4.50:
            return 'A'
        elif value >= 3.0 and value < 3.5:
            return 'A-'
        elif value >= 2.5 and value < 3.0:
            return 'B'
        elif value >= 2.0 and value < 2.5:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return 'F'
        

        # Represents a classroom
    def __repr__(self) -> str:
        # All Classroom
        # All Teachers
        # All Students
        # All Subjects
        # All Students Results
        pass