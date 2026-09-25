import numpy as np

students  = np.array([
    [70, 80, 65],
    [85, 72, 90],
    [60, 75, 68],
    [92, 88, 81],
    [55, 64, 70]
])
average = np.mean(students)
print(average)
score = students > average
print(students[score])
