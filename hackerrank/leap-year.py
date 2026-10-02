def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 400 == 0:
        leap = bool(True)
        return leap
    elif year % 100 == 0:
        leap = bool(False)
        return leap

while True:
    try:
        year = int(input("Enter a year: "))
        if 1900 <= year <= 1000000:
            break
        else:
            print("Input out of range.")
    except ValueError:
        print("Invalid input. Enter a year.")

print(is_leap(year))