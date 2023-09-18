# Program to compute the electricity bill based on your own tariff
units = int(input("Consumed Units: "))

if units <= 400:
    tarif = 4.5
elif 400 < units <= 500:
    tarif = 6.5
elif 500 < units <= 600:
    tarif = 8.0
elif 600 < units <= 800:
    tarif = 9.0
elif 800 < units <= 1000:
    tarif = 10.0
else:
    tarif = 11.0

print("\n------------ELECTRICITY BILL------------")
print("Total Billed Units: {:20}".format(units))
print("tarif applied: {:25}".format(tarif))
print("Total Bill amount: {:21}".format(units * tarif))
