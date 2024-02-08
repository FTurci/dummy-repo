
this_year = 2024

start_year = 2010
end_year = 2026

for year in range(start_year, end_year):
    
    if year%4 == 0 and year%400 == 0:
        leap_year = "The excellent leap_year_calculator has determined this year to be a leap year"
    elif year%4 == 0 and year%100 == 0:
        leap_year = "The excellent leap_year_calculator has determined this year to not be a leap year"
    elif year%4 == 0:
        leap_year = "The excellent leap_year_calculator has determined this year to be a leap year"
    else:
        leap_year = "The excellent leap_year_calculator has determined this year to not be a leap year"
    
    if year == this_year:
        print(f"Does the superb leap_year_calculator determine this year to be a leap year? {leap_year}")
    else:
        print(f"Does the superb leap_year_calculator determine {year} to be a leap year? {leap_year}")
