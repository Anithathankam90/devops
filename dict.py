person = {'name': 'Anitha', 'course': 'devops'}

print('Name: ', person.get('name'))
print('Course: ', person.get('course'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0)) 
