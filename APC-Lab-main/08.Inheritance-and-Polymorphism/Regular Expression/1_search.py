import re

pattern = re.compile("python")
text = "I am learning python programming"

result = pattern.search(text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")