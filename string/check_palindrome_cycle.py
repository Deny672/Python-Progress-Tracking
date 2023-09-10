def check_palindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[-i - 1]:
            return 'Is not palindrome'

    return 'Is palindrome'


text = '12344321'

print(check_palindrome(text))