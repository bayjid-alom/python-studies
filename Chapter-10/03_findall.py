import re

text_1 = "The rain in Spain"
result_1 = re.findall("ai", text_1)

text_2 = "Python is easy. Python is powerful. Python is popular."
result_2 = re.findall("is", text_2)

print(result_1)
# ['ai', 'ai']

print(result_2)
# ['is', 'is', 'is']
