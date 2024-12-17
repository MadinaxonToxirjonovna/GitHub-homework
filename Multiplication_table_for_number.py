def multi_table(number):
    result = ""
    for i in range(1, 11):
        result += f"{i} * {number} = {i * number}\n"
    return result
number = 5
a = multi_table(number)
print(a)