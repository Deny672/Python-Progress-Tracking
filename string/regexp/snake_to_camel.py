import re

def convert_to_camel_case(match):
    return match.group(1).capitalize()

text_normal = "some_text_in_snake_notation"

pattern = re.sub(r'_([a-zA-Z])', convert_to_camel_case, text_normal)
print(pattern)