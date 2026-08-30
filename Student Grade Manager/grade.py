import json
def load_student_grade():
     try:
          with open ("student_details.json", "r") as file:
               student_details = json.load(file)
               return student_details
     except FileNotFoundError:
          return []

def save_student_grade():
     with open ("student_details.json", "w") as file:
          json.dump(student_details, file)


def get_valid_grade(subject):
     while True:
          try:
               grade = float(input(f"Enter Grade for {subject}: "))
          except ValueError:
               print("Invalid input. Try again")
               continue
          if grade < 0 or grade > 100:
               print("Grade must be between 0 and 100")
          else:
               return grade

def find_student(name):
     for student in student_details:
          if name.lower() == student["Name"].lower():
               return student
     return None
def add_students():
    student_name = input("Enter Student name: ")
    student_class = input("Enter Student Class: ")
    try:
         number_of_subjects = int(input("How many subjects are you offering: "))
    except ValueError:
         print("Invalid input. Try Again")
         return
    if number_of_subjects <= 0:
         print("Number must be greater than zero")
         return
    grades = {}
    for _ in range(number_of_subjects):
         subject = input("Enter Subject: ")
         if any(subject.lower() == existing_subject.lower() for existing_subject in grades):
              print("That subject has already been added")
              return
         grade_value = get_valid_grade(subject)
         grades[subject] = grade_value
         
    student = {"Name": student_name, "Class": student_class, "Grades": grades}
    student_details.append(student)
    save_student_grade()
    print("You have successfully added a student grade")

def view_students():
     if not student_details:
          print("No Student grades found")
     else:
          for index, student in enumerate(student_details, start=1):
               print(f"{index}. {student['Name']}")
               print(f"Class: {student['Class']}")
               for subject, grade in student["Grades"].items():
                    print(f"      {subject}: {grade}")

def search_student():
      search_name = input("Enter the name of the student: ")
      student = find_student(search_name)
      if student is None:
           print(f"{search_name} not found")
           return
      print(f"Name: {student['Name']}")
      print(f"Class: {student['Class']}")
      for subject, grade in student["Grades"].items():
            print(f"     {subject}: {grade}")
      

def calc_avg():
      student_avg = input("Enter the Student name: ")
      avg = 0
      found = False
      for student in student_details:
            if student_avg.lower() == student["Name"].lower():
                 found = True
                 for grade in student["Grades"].values():
                       avg += grade

                 average = avg / len(student["Grades"])
                 print(f"Average: {average}")
      if not found:
           print(f"{student_avg} not found")

def calc_grade():
      student_grade = input("Enter the Student name: ")
      found = False
      avg = 0
      for student in student_details:
            if student_grade.lower() == student["Name"].lower():
                found = True
                for grade in student["Grades"].values():
                      avg += grade
      
                average = avg / len(student["Grades"])
                if average >= 90:
                      grade = "A"
                      
                elif average >= 80:
                      grade = "B"
                      
                elif average >= 70:
                      grade = "C"
                      
                elif average >= 60:
                      grade = "D"
                
                else:
                      grade = "F"
                print(f"Student: {student['Name']}")
                print(f"Class: {student['Class']}")
                print(f"Average: {average}")
                print(f"Grade: {grade}")
      if not found:
            print(f"{student_grade} not found")

def update_student_grade():
      found = False
      if not student_details:
            print("No student found")
      else:
            for index, student in enumerate(student_details, start=1):
                print(f"{index}. {student['Name']}")
                print(f"         Class: {student['Class']}")
                for subject, grade in student["Grades"].items():
                    print(f"      {subject}: {grade}")

            update_grade = input("Enter the student name: ")
            for student in student_details:
                if update_grade.lower() == student["Name"].lower():
                    found = True
                    update_subject = input("Enter the Subject: ")
                    seen = False
                    for subject in student["Grades"]:
                        if update_subject.lower() == subject.lower():
                            seen = True
                            
                            new_grade = get_valid_grade(subject)
                            student["Grades"][subject] = new_grade
                            save_student_grade()
                            print("Grade has been updated successfully")
                            break
                    if not seen:
                        print(f"{update_subject} is not a valid subject")
      if not found:
            print("Student not found")

def remove_student():
      if not student_details:
            print("No student found")
      else:
            for index, student in enumerate(student_details, start=1):
                print(f"{index}. {student['Name']}")
                print(f"         Class: {student['Class']}")
                for subject, grade in student["Grades"].items():
                    print(f"      {subject}: {grade}")

            try:
                student_number = int(input("Enter the student number you want to remove: "))      
            except ValueError:    
                print("Invalid input. Try again")
                return          
            if student_number < 1 or student_number > len(student_details):
                  print("Invalid Input. Try again")
                  return
            else:
               student_index = student_number - 1
               removed_student = student_details[student_index]
               student_details.pop(student_index)
               save_student_grade()
               print(f"{removed_student['Name']} was removed successfully")

student_details = load_student_grade()
choice = ""
while choice != "8":
      print("===== STUDENT GRADE MANAGER =====")
      print("1. Add Student")
      print("2. View Students")
      print("3. Search Student")
      print("4. Calculate Average")
      print("5. Calculate Grade")
      print("6. Update Student Grade")
      print("7. Remove Student")
      print("8. Exit")

      choice = input("Enter your choice (1 - 8): ")

      match choice:
            case "1":
                  add_students()
            case "2":
                  view_students()
            case "3":
                  search_student()
            case "4":
                  calc_avg()
            case "5":
                  calc_grade()
            case "6":
                  update_student_grade()
            case "7":
                  remove_student()
            case "8":
                  print("Exiting the program.")
            case _:
                  print("Invalid choice. try again")