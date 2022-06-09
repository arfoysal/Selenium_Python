# function which return reverse of a string
'''
def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")


def isPalindrome(s):
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

'''
x = "maaalayalam"

w = ""
for i in x:
    w = i + w
    print(w)

if x == w:
    print("Yes")
else:
    print("No")