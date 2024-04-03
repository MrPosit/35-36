class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    def get_average_grade(self):
        return self.average_grade

    def display_information(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}")


class SeniorStudent(Student):
    def __init__(self, name, age, average_grade, thesis_title):
        super().__init__(name, age, average_grade)
        self.thesis_title = thesis_title

    def set_thesis_title(self, thesis_title):
        self.thesis_title = thesis_title

    def get_thesis_title(self):
        return self.thesis_title

student1 = Student("John Doe", 20, 4.5)
student1.display_information()

senior_student1 = SeniorStudent("Jane Smith", 22, 4.8, "Research on Artificial Intelligence")
senior_student1.display_information()
print(f"Название дипломной работы: {senior_student1.get_thesis_title()}")
