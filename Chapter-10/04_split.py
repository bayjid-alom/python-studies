import re

text = "Python, Java, JavaScript, C, C++, C#, Go, Rust, Swift, Kotlin, TypeScript, PHP, Ruby"

result = re.split(",", text)

print(result)


"""
['Python', ' Java', ' JavaScript', ' C', ' C++', ' C#', ' Go', ' Rust', ' Swift', ' Kotlin', ' TypeScript', ' PHP', ' Ruby']

"""
