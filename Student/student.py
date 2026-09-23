class Student:
    def __init__(self, name, age, student_id, department):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.department = department
        self.subjects = {}

    # Display Info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")
        print("Subjects:")
        for subject, score in self.subjects.items():
            print(f"{subject}: {score}")
        print(f"Average: {self.calc_average()}")
        print(f"Grade: {self.get_grade()}")

    # Add Subject
    def add_subject(self, subject, score):
        subject = subject.strip().lower()
        if not subject:
            raise ValueError("Subject cannot be empty")
        if subject in self.subjects:
            raise ValueError("Subject already exists.")
        if not isinstance(score, int) or score < 0 or score > 100:
            raise ValueError("Score must be an integer between 0 and 100.")
        self.subjects[subject] = score

    # Calculate Average
    def calc_average(self):
        if len(self.subjects) == 0:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    # Get Grade
    def get_grade(self):
        average = self.calc_average()
        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 45:
            return "D"
        elif average >= 40:
            return "E"
        else:
            return "F"

    # Setters and Getters for Age 
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age <= 0:
            raise ValueError("Age must be positive.")
        self._age = new_age

    # Setter & Getter for Department 
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        if not new_department:
            raise ValueError("Department cannot be empty")
        self._department = new_department

    # Student Manager
class StudentManager:
    def __init__(self):
        self.students = {}

    # ADD STUDENT
    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student.student_id] = student

    # FIND STUDENT
    def find_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        return self.students[student_id]

    # REMOVE STUDENT
    def remove_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        del self.students[student_id]

    # LIST STUDENT
    def list_students(self):
        for student_id, student in self.students.items():
            print(f"{student_id} - {student.name}")
        
    # UPDATE STUDENT 
    def update_student(self, student_id, department=None, age=None):
        student = self.find_student(student_id)
        if department is None and age is None:
            print("Nothing to update.")
            return

        if department is not None:
            student.department = department

        if age is not None:
            student.age = age

        print("Student updated successfully")


student1 = Student("Prince", 20, "ST002", "Computer Science")
manager = StudentManager()
manager.add_student(student1)
manager.update_student("ST002", department="Data Science")
manager.update_student("ST002", age=21)
manager.list_students()