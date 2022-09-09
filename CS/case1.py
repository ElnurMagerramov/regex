import re
Nameage = "\
Janice is 22 and Theon is 33 \
Gabriel is 44 and Joey is 21\
"
names=re.findall("[A-Z]\w+", Nameage)
ages=re.findall("[0-9]\w+", Nameage)
dictionary=dict(zip(names,ages))
print(dictionary)