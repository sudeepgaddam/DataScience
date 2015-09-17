import Levenshtein as L
import pandas as pd

Students = pd.DataFrame({'student_id': [1, 2], 'name': ['Alice', 'Bob']})
Grades = pd.DataFrame({'student_id': [1, 1, 2, 2], 'class_id': [1, 2, 1, 3], 'grade': ['A', 'C', 'B', 'B']})
Classes = pd.DataFrame({'class_id': [1, 2, 3], 'title': ['Math', 'English', 'Spanish']})
Stud_Grades = pd.merge(Students, Grades, on='student_id')
StudentGradesClasses = pd.merge(Stud_Grades, Classes, on='class_id')
is_alice = (StudentGradesClasses['name'] == 'Alice') & (StudentGradesClasses['grade'] == 'A')
print StudentGradesClasses[is_alice]['title']
