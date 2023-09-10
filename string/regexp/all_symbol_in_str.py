import re

text_normal = "Ліна Василівна @Кос$тенко (нар. 19 березня 1930),!"

pattern = r"[^\w\s]"
text_with_num = re.findall(pattern, text_normal)
print(text_with_num)