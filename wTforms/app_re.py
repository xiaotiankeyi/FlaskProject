import re

a = re.match(r"^[0-9a-zA-Z]\w{6,12}$", 'a123456lai_')
print(a.group())