import re

# task 3
def end_str(string, text):
    if text.match(string):
        return True
    else:
        return False

print(end_str('abcdef', re.compile(r".*[0-9]$")))
print(end_str('abcdef6', re.compile(r".*[0-9]$")))


myString="!elnur? ddzsSikkhmji"
# task 4

pattern=r"[?!]\b\w+"

result1 = re.findall(pattern, myString)
print(result1)



# task 5
result2=re.sub("\s", "  ", myString)
print(result2)
result3=result2.replace ("  ", " ")
print(result3)

# task 6
myString_large="Lorem, ipsum dolor üit amet consectetur adipisicing elit. üodi totam odit voluptatibus üxercitationem ab, reiciendis aoluptas! Eveniet porro ratione, araesentium beatae un?de, soluta, tempora commodi illum sit doloribus optio nobis.?"
pattern_for_large = r"\b[aü]\w+"
result_large = re.findall(pattern_for_large, myString_large)
print(result_large)


# task 7
print(re.sub("\s", "", myString_large))

# task 8
print(re.findall("[a-zA-Z]{4}\w+", myString_large))


# task 9
pattern_capital_letter=r"(\w)([A-Z])"
str = "AsssSDFGHsxsJKsxxzdHSJ"
result_capital_letter=re.sub(pattern_capital_letter, r"\1 \2", str)
print(result_capital_letter)