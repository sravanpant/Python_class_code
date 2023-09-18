import locale as lc

# from decimal import Decimal

# lc.setlocale(lc.LC_ALL, "en_US.utf8")

# monthly_investment = float(input("Enter monthly investment:   "))
# yearly_interest = float(input("Enter yearly interest rate: "))
# years = int(input("Enter number of years:      "))

# future_value = 0
# monthly_interest_rate = yearly_interest / 12 / 100
# months = years * 12
# for i in range(months):
#     future_value += monthly_investment
#     monthly_interest = future_value * monthly_interest_rate
#     future_value += monthly_interest

# monthly_investment = str(
#     lc.currency(Decimal(monthly_investment).quantize(Decimal(".01")), grouping=True)
# )

# future_value = str(
#     lc.currency(Decimal(future_value).quantize(Decimal(".01")), grouping=True)
# )
# print("\nMonthly Investment: " + " " * 4 + monthly_investment)
# print("Interest Rate: {:16}".format(Decimal(yearly_interest).quantize(Decimal(".01"))))
# print("Years: {:24}".format(years))
# print("Future Value: " + " " * 7 + future_value)

print(lc.format_string("%.2f", 12345.67, grouping=True))
