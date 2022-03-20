nomarat=[]

students_numbers = int(input('Tedade daneshjoyan ra vared konid: '))
for i in range(students_numbers):
    scores = int(input('nomre ra vared konid: '))
    nomarat.append(scores)

miyangin = sum(nomarat)/len(nomarat)

print(max(nomarat),min(nomarat),miyangin)