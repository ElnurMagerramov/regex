import re

pattern="\w+[aıoueəiöü]\w+"

result = re.findall(pattern,"salam dunya ssss")
print(result)