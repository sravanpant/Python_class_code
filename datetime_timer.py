from datetime import date, time, datetime

print("The Timer program\n")
if not input("Press Enter to start..."):
    start_time = datetime.now()
    print("Start time:", start_time, "\n")

if not input("Press Enter to stop..."):
    stop_time = datetime.now()
    print("Stop time:", stop_time, "\n")

elapsed_time = stop_time - start_time
print("ELAPSED TIME")
print("Time:", elapsed_time)
