import matplotlib.pyplot as plt

students = ["Sammy", "John", "Mary", "David", "Sarah"]
scores = [75, 82, 68, 90, 85]

plt.bar(students, scores)

plt.title("Exam Scores")
plt.xlabel("Students")
plt.ylabel("Scores")

plt.show()