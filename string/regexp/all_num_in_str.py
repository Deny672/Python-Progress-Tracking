import re

text_normal = "Ліна Василівна Костенко (нар. 19 березня 1930)"

pattern = r"[0-9]+"
text_with_num = re.findall(pattern, text_normal)
print(text_with_num)