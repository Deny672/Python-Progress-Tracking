import re

text_normal = "' ; dsadas asdasd asd 2022-01-22 adasd ads sa 2023-04-23, 231313-2313-3131'"

pattern = r"\d+-\d{2}-\d{2}"
text_with_num = re.findall(pattern, text_normal)
print(text_with_num)