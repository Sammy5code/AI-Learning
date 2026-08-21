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

def add_students():
    student_name = input("Enter Student name: ")

    try:
        math_grade = float(input("Enter Mathematics Grade: "))
    except ValueError:
        print("Invalid input. Please try again")
        return

    if math_grade < 0 or math_grade > 100:
        print("Grade must be between 0 and 100")
        return
    
    try:
         english_grade = float(input("Enter English-Language Grade: "))
    except ValueError:
            print("Invalid input. Please try again")
            return

    if english_grade < 0 or english_grade > 100:
        print("Grade must be between 0 and 100")
        return
    
    try:
         python_grade = float(input("Enter Python Grade: "))
    except ValueError:
            print("Invalid input. Please try again")
            return
    
    if python_grade < 0 or python_grade > 100:
            print("Grade must be between 0 and 100")
            return
    
    grade = {"Math": math_grade, "English": english_grade, "Python": python_grade}
    student = {"Name": student_name}
    student["Grades"] = grade
    student_details.append(student)
    save_student_grade()
    print("You have successfully added a student grade")

def view_students():
     if not student_details:
          print("No Student grades found")
     else:
          for index, student in enumerate(student_details, start=1):
               print(f"{index}. {student['Name']}")
               for subject, grade in student["Grades"].items():
                    print(f"      {subject}: {grade}")

def search_student():
      search_name = input("Enter the Student name: ")
      found = False
      for student in student_details:
            if search_name.lower() == student["Name"].lower():
                  found = True
                  print(f"Name: {student['Name']}")
                  for subject, grade in student["Grades"].items():
                        print(f"     {subject}: {grade}")
      if not found:
            print(f"{search_name} not found")

def calc_avg():
      student_avg = input("Enter the Student name: ")
      avg = 0
      for student in student_details:
            if student_avg.lower() == student["Name"].lower():
                 for grade in student["Grades"].values():
                       avg += grade

                 average = avg / len(student["Grades"])
                 print(f"Average: {average}")

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
                print(f"Average: {average}")
                print(f"Grade: {grade}")
      if not found:
            print(f"{student_grade} not found")

def update_student_grade():
      if not student_details:
            print("No student foound")
      else:
            for index, student in enumerate(student_details, start=1):
                print(f"{index}. {student['Name']}")
                for subject, grade in student["Grades"].items():
                    print(f"      {subject}: {grade}")

            update_grade = input("Enter the student name: ")
            found = False
            for student in student_details:
                if update_grade.lower() == student["Name"].lower():
                    found = True
                    update_subject = input("Enter the Subject: ")
                    seen = False
                    for subject in student["Grades"]:
                        if update_subject.lower() == subject.lower():
                            seen = True
                            try:
                                new_grade = float(input("Enter new Grade:"))
                            except ValueError:
                                print("Invalid Input. Try Again")
                                return
                            if new_grade < 0 or new_grade > 100:
                                print("Grade must be between 0 and 100")
                                return
                            student["Grades"][subject] = new_grade
                            save_student_grade()
                            print("Grade has been updated successfully")
                            break
                    if not seen:
                        print(f"{update_subject} is not a valid subject")
      if not found:
            print("Student no found")

def remove_student():
      if not student_details:
            print("No student found")
      else:
            for index, student in enumerate(student_details, start=1):
                print(f"{index}. {student['Name']}")
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