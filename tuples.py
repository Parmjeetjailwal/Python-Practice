# tuple = Collection which is ordered and unchangeable
#         used to group together related data

student= ("Parm", 25, "male")

print(student.count("Parm")) 
print(student.index("male")) 

for i in student:
    print(i)

if "Parm" in student:
    print("Parm is here!")
