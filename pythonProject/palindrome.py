def is_palindrome(s):
    #replace places and lowercase
    s=s.replace(" "," ").lower()
    return s == s[::-1]
print(is_palindrome("Amma"))


