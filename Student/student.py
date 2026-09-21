class Student:
    def __init__(self, name, age, student_id, department):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.department = department
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age <= 0:
            raise ValueError("Age must be positive.")
        self._age = new_age

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        if not new_department:
            raise ValueError("Department cannot be empty")
        self._department = new_department


student1 = Student("Prince", 20, "ST002", "Computer Science")
print(student1.department)
student1.department = "Data Science"
print(student1.department)