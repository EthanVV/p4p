with open('students.csv') as fin:
  for line in fin:
    record = line.strip()
    validate(record)

def validate(record):
  name, q1, q2, q3, q4, grade = record.split(',')
  scores = [int(score) for score in [q1, q2, q3, q4]]
  average_score = sum(scores) / len(scores)
  if assign_grade(avg) != grade:
    print(name)

def assign_grade(avg):
  if 100 >= ave >= 90:
    return 'A'
  elif avg >= 80:
    return 'B'
  elif avg >= 70:
    return 'C'
  elif avg >= 60:
    return 'D'
  else: 
    return 'F'
