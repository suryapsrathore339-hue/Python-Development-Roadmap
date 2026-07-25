from collections import Counter
text="mississippi"
count=Counter(text)
print(count)

words = ["AI", "ML", "AI", "Python", "ML", "AI"]
count=Counter(words)
print(count)
print(count['AI'])

from collections import defaultdict

d = defaultdict(list)

d["AI"].append("Python")
d["AI"].append("Machine Learning")
d["Web"].append("FastAPI")

print(d)