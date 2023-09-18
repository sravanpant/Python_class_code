def Sumofdigit(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return f"Sum of digits: {sum}"


def Revdigit(num):
    reverse_num = 0
    while num != 0:
        reverse_num = reverse_num * 10 + (num % 10)
        num = num // 10
    return f"The reversed number: {reverse_num}"


# print(Sumofdigit(1234))
# print(Revdigit(1234))
