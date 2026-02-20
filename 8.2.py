def is_palindrome(text):

        text = text.lower()

        cleaned_text = ''
        for char in text:
            if char.isalnum():
                cleaned_text += char

        return cleaned_text == cleaned_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
