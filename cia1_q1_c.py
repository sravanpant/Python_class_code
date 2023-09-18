def GCD(a, b):
    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return f"GCD: {result}"


def ReversingANumber(num):
    reverse_num = 0
    while num < 0:
        reverse_num = reverse_num * 10 + num % 10
        num = num // 10
    return f"Reversed Number: {reverse_num}"
