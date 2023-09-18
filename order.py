from decimal import Decimal, ROUND_HALF_UP

order = float(input("Enter order total: "))
print()
if 100 <= order <= 250:
    discount = 0.1 * order
elif order > 250:
    discount = 0.2 * order
tax = 0.05 * (order - discount)

print(
    "Order total: {:14}".format(Decimal(order).quantize(Decimal(".01"), ROUND_HALF_UP))
)
print(
    "Discount amount: {:10}".format(
        Decimal(discount).quantize(Decimal(".01"), ROUND_HALF_UP)
    )
)
print(
    "Subtotal: {:17}".format(
        Decimal(order - discount).quantize(Decimal(".01"), ROUND_HALF_UP)
    )
)
print("Sales tax: {:16}".format(Decimal(tax).quantize(Decimal(".01"), ROUND_HALF_UP)))
print(
    "Invoice total: {:12}".format(
        Decimal(order - discount + tax).quantize(Decimal(".01"), ROUND_HALF_UP)
    )
)

option = input("\nContinue? (y/n): ")
