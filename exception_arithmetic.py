def calculator(op1: float, op2: float, op: str) -> float:
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        if op2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return op1 / op2
    elif op == "//":
        if op2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return op1 // op2
    elif op == "%":
        if op2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return op1 % op2
    else:
        raise ValueError("Unknown operator")


try:
    op1 = float(input("Enter first operand: "))
    op2 = float(input("Enter second operand: "))
    op = input("Enter operator: ")
    print(f"{op1} {op} {op2} = {calculator(op1, op2, op)}")
except ValueError as msg:
    print(msg)
except ZeroDivisionError as msg:
    print(msg)
