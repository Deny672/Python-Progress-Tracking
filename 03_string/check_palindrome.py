def check_palindrome(str):
    reversed_str = str[::-1]

    if str == reversed_str:
        return True
    else:
        return False


text = '123445321'

print(check_palindrome(text))