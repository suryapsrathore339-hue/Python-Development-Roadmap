names=["Surya","Ravi","Ramesh"]
ages=[25,30,35]
for name, age in zip(names, ages):
    print(name,age)

languages=["Python","Java","C++"]
for index, language in enumerate(languages):
    print(index,language)

languages=["Python","Java","C++"]
for index, language in enumerate(languages, start=1):
    print(index,language)

subjects=["Maths","Chemistry","Physics"]
marks=[90,80,70]

for index, (subject, mark) in enumerate(zip(subjects, marks), start=1):
    print((index, subject, mark))