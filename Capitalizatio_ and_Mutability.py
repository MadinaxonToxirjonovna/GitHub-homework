def capitalize_word (word : str) -> str:
    return word[0].upper() + word[1:]
word = "hello"
a = capitalize_word(word)
print(a)