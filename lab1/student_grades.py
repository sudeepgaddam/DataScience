import Levenshtein as L
import pandas as pd

Students = pd.DataFrame({'student_id': [1, 2], 'name': ['Alice', 'Bob']})
#print Students
Grades = pd.DataFrame({'student_id': [1, 1, 2, 2], 'class_id': [1, 2, 1, 3], 'grade': ['A', 'C', 'B', 'B']})
#print Grades
Stud_Grades = pd.merge(Students, Grades, on='student_id')
print Stud_Grades
is_alice = (Stud_Grades['name'] == 'Alice') & (Stud_Grades['grade'] == 'A')
print Stud_Grades[is_alice]
