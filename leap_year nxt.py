def is_leap(year):
    if year % 4 == 0:
        
        if year % 100 == 0:
            
            if year % 5 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False
def days_in_month(year,month):
    """It takes the values of a year and a month and returns the number of days in that year"""
    if is_leap(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not is_leap(year):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]
year = int(input("Enter the year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)

print(days)