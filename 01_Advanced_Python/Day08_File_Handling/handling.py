file=open("students.txt","w")
file.write("Hello Surya")
file.close()

file=open("students.txt","a")
file.write("\nHello Shreya")
file.close()

file=open("students.txt","r")
content=file.read()
print(content)
file.close()

file=open("notes.txt","w")
file.write("Hello Surya")
file.close()

file=open("notes.txt","a")
note=input("Enter your note:")
file.write("\n"+note)
file.close()

file=open("notes.txt","r")
content=file.read()
print(content)
file.close()