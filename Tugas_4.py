kata = ['rotator']

def is_plndr(x):
    if x == x[::-1]:
        print(True)
    else:
        print(False)

palindrome = list(filter(is_plndr,kata))
print(palindrome)