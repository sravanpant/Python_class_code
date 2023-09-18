from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN

print(Decimal("7.9").quantize(Decimal("1"), rounding=ROUND_HALF_DOWN))
print(Decimal("7.33").quantize(Decimal("0.01"), rounding=ROUND_HALF_DOWN))
print(Decimal("1.23").quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
