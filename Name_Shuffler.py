def name_shuffler(str_):
    a = str_.split()
    if len(a) == 2:
        return f"{a[1]} {a[0]}"
str_ = "john McClane"
b = name_shuffler(str_)
print(b)