from datetime import date, time, datetime

print("The Invoice Due Date program\n")
invoice_date = input("Enter the invoice date (MM/DD/YY): ")
month, day, year = invoice_date.split("/")
invoice_date = datetime(int(year), int(month), int(day))
due_date = datetime(2023, 9, 5)
current_date = datetime.now()
overdue_days = (current_date - due_date).days
print("\nInvoice Date:", invoice_date.strftime("%B %d, %Y"))
print("Due Date:", due_date.strftime("%B %d, %Y"))
print("Current Date:", current_date.strftime("%B %d, %Y"))

print("\nThis invoice is", overdue_days, "day(s) overdue.\n")
print("Continue? (y/n):")
