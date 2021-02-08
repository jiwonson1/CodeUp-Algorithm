import re

string = input()
print(re.sub(r'\s+', '', string))
