import re

text_normal = "someTextInSnakeNotation"

pattern = re.sub(r"([A-Z])", r"_\1", text_normal).lower()
print(pattern)