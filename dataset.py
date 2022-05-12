school = {'students': [{'name': 'Annie', 'age': 11, 'score': 'A+'},
                       {'name': 'Bobby', 'age': 13, 'score': 'B'},
                       {'name': 'Carla', 'age': 14, 'score': 'B-'},
                       {'name': 'David', 'age': 12, 'score': 'A'}],
          'teachers': [{'name': 'Mr B', 'subject': 'Math', 'grade': '6th'},
                       {'name': 'Mrs P', 'subject': 'Art', 'grade': '5th'}]}

school['students'].append({'name': 'Eric', 'age': 11, 'score': 'A'})

total_students = len(school['students'])
total_teachers = len(school['teachers'])

print('There are %s students' % total_students)
print('There are %s teachers' % total_teachers)

total_age = 0

for i in range(0, total_students):
    total_age = total_age + school['students'][i]['age']
    
av_age = total_age / total_students
print('Average student age is %s years old' % av_age)