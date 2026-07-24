import json 
student={
    "Name":"Surya",
    "Age":20,
    "College":"IIITDMJ"
}

with open("student.json","w") as file:
    json.dump(student,file,indent=4)

with open("student.json","r") as file:
    data=json.load(file)

print(data)
print(type(data))

# 1.Json->Python String
# 2.Python String->Json
# 3.Python Object->JSON File
# 4.Reads the json file

# 1.b)underfitting
# 2.b)overfitting
# 3.b)High variance
# 4.b)High bias
# 5.because we need to maintain the model well so that it learns well from training data and performs well on unseen data.