import re
myString="elnur ddikkhmji"

pattern=r"[^(a|ı|o|u|e|ə|i|ö|ü)]"
result = re.findall(pattern, myString)
print(result)
