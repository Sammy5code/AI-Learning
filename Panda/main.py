import pandas as pd

df = pd.read_csv("student_data.csv")

# df = df.drop(columns=["math_score", "attendance"])

#2 Handle Missing Data 

# df = df.dropna(subset=["english_score"])

# df = df.fillna({"english_score": })

# df["name"] = df["name"].replace({"Daniel": "DANIEL", "David": "DAVID"})

# 4. Standardize text
# df["name"] = df["name"].str.lower()Isabella,21,Mathematics,Female,88,91,86,96,A

# 5. Fix data types
# df["grade"] = df["grade"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()
print(df.to_string())