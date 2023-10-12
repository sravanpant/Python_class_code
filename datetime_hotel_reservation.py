from datetime import date, time, datetime

print("The Hotel Reservation program\n")
while True:
    try:
        arrival_date = input("Enter arrival date (YYYY-MM-DD): ")
        ar_year, ar_month, ar_day = arrival_date.split("-")
        arrival_date = date(int(ar_year), int(ar_month), int(ar_day))

        departure_date = input("Enter departure date (YYYY-MM-DD): ")
        dp_year, dp_month, dp_day = departure_date.split("-")
        departure_date = date(int(dp_year), int(dp_month), int(dp_day))

        if ar_month == dp_month:
            if ar_month in ["4", "5", "8", "9"]:
                cost = 105.00
            else:
                cost = 85.00
            total_days = int(dp_day) - int(ar_day)
            total_cost = total_days * cost

        print("\nArrival Date:", arrival_date.strftime("%B %d, %Y"))
        print("Departure Date:", departure_date.strftime("%B %d, %Y"))
        if ar_month in ["4", "5", "8", "9"]:
            print("Nightly rate: $" + str(cost) + " (High season)")
        else:
            print("Nightly rate: $" + str(cost))

        print("Total nights:", total_days)
        print("Total Price: $" + str(total_cost))
        choice = input("\nContinue? (y/n): ")
        if choice == "y":
            continue
        elif choice == "n":
            print("\nBye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue
    except ValueError:
        print("Invalid date")
        break
