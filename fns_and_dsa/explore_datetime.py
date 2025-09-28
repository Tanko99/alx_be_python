# explore_datetime.py
from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format nicely
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return it in case we need it later

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input! Please enter an integer number of days.")
        return
    
    future_date = current_date + timedelta(days=days_to_add)  # Add days
    formatted_future = future_date.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
    print(f"Future date: {formatted_future}")

def main():
    current_date = display_current_datetime()  # Part 1
    calculate_future_date(current_date)        # Part 2

if __name__ == "__main__":
    main()
