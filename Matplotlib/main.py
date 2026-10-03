import pandas as pd 
import matplotlib.pyplot as plt 

data = {
    "Student": ["Sammy", "John", "Mary", "David", "Sarah"],
    "Score": [75, 82, 68, 90, 85]
}

df = pd.DataFrame(data)

plt.bar(df["Student"], df["Score"])

plt.title("Exam Score")
plt.xlabel("Students")
plt.ylabel("Scores")

plt.show()