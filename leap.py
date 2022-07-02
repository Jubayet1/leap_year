def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year"
      else:
        return "Not leap year"
    else:
      return "Leap year"
  else:
    return "Not leap year"

def days_in_month(year, month):
  year = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  days = month_days[month-1]
  if year == 'Leap year' and month == 2:
    days = 29
  else:
    days = month_days[month-1]
  return f'It is {year} and {month}th month has {days}'
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)