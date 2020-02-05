file_names = ['course-list1.txt', 'course-list2.txt', 'course-list3.txt']

def get_courses(file_name):
  file_data = open(file_name, encoding='utf-8').read().split('\n')
  course_dict = {}

  for line in file_data:
    if ('unit' in line):
      name, unit_val = line.rsplit(',', 1)
      name = name.strip()
      unit_val = unit_val.strip()
      if course_dict.get(name) == None:
        course_dict[name] = unit_val

  return course_dict

def hamming_distance(value1, value2):
  distance = 0

  for i in range(0, min(len(value1), len(value2))):
    if value1[i] != value2[i]: distance += 1

  return distance


course_dict = {}
repeat_courses = {}

for file in file_names:
  read_courses = get_courses(file)

  for key in read_courses.keys():
    if key in course_dict.keys():
      repeat_courses[key] = read_courses[key]
    else: 
      course_dict[key] = read_courses[key]

for course in repeat_courses: print(course)

print(hamming_distance('karolin', 'kathrin'))
print(hamming_distance('karolin', 'kerstin'))