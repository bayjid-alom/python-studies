import re

text = "I love Python Programming"

result = re.search("Python", text)

print(result)
# <re.Match object; span=(7, 13), match='Python'>


print(result.group())
# Python
