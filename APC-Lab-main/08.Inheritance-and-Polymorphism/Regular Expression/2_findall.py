import re

text = "My marks are 85, 92 and 78"

numbers = re.findall(r'\d+', text)

print("Numbers:", numbers)