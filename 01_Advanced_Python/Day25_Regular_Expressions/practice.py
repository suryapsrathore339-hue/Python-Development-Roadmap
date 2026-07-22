import re
text="I m Learning Python"
result=re.search("Python",text)
if result:
    print("found!")
else:
    print("Not found!")

text = "AI ML AI Python AI"
result=re.findall("AI",text)
print(result)

text = "Hello Surya"
result=re.match("Hello",text)
if result:
    print("Match found")
else:
    print("Match not found")