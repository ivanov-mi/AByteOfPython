def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text.lower() == reverse(text).lower()

ignoredSymbols = ('!?., ')

inputText = input("Enter text: ")
punctuationIgnoredText = inputText.translate(({ord(i): None for i in ignoredSymbols}))

if is_palindrome(punctuationIgnoredText):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")