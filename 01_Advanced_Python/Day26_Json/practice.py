import json

student={
    "name":"Surya",
    "age":20,
    "branch":"Smart Manufacturing"
}
result=json.dumps(student)
print(result)

data='{"city":"Jabalpur","state":"Madhya Pradesh"}'
result=json.loads(data)
print(result)
print(type(result))

# json.dumps()-python to json string
# json.loads()-json string to python