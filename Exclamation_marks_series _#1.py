def remove(s):
    if s and s[-1] == "!":
        return s[:-1]
    return s
s = 'Hi!'
print(remove(s))