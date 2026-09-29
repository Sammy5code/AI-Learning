import pandas as pd 

student = pd.read_csv("student_data.csv")

print(student.head())
print(student.shape)
print(student.info())
print(student[["name", "math_score"]])

print(student.sort_values(by="math_score", ascending=False))