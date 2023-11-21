def is_palindrome(phrase):
    phrase = phrase.lower()

    if phrase == phrase[::-1]:
        return True
    else:
        return False
