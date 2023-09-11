import re

text_normal = 'some text with hex #ABCDEF colors like this #fff'

pattern = r"#([A-Fa-f\d]{3,8})"
text_with_num = re.findall(pattern, text_normal)
print(text_with_num)