from pathlib import Path

# Create a path object
path=Path("students.txt")

# check if it exists
print(path.exists())

# check if it is a file
print(path.is_file())

# Print all python files in a current directory
for file in Path(".").glob("*.py"):
    print(file)

# output
# PS C:\Users\Surya Rathore\OneDrive\Desktop\Python-Development-Roadmap> python -u "c:\Users\Surya Rathore\OneDrive\Desktop\Python-Development-Roadmap\01_Advanced_Python\Day32_Pathlib\practice.py"
# True
# True

# 1.b)datetime
# 2.b)date.today()
# 3.b)strftime()
# 4.c)Four-digit-Year