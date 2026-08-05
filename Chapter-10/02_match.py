"""
re.match() String-এর শুরু (Beginning) থেকে Pattern Match করে; শুরুতেই Match না হলে None Return করে।
"""

import re

sentence = "Hello Programmers"
result = re.match("Java", sentence)

print(result)
# None

# print(result.group())
# Error দিবে । কারণ, ম্যাচ করেনি তাই কোনো স্ট্রিং নেই ।


line = "Bangladesh is our country"
output = re.match("Bangladesh", line)

print(output)
# <re.Match object; span=(0, 10), match='Bangladesh'>

print(output.group())
# Bangladesh
