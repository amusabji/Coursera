"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    # subtract first day of the month with first day of following month
    # to get number of days in that month using datetime module's date function
    # if current month is 12, day is 31, otherwise calculate to avoid potential off by 1 error.
    current_month_obj = datetime.date(year, month, 1)
    if month == 12:
        return 31
    else:
        next_month_int = month + 1
        next_month_obj = datetime.date(year, next_month_int, 1)
        days_current_month = next_month_obj - current_month_obj
        return days_current_month.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """

    ## perform sequential checks for 1 input variable at a time.

    # Validate year
    if ((year > datetime.MAXYEAR) or (year < datetime.MINYEAR)):
        return False

    # Validate month
    if ((month > 12) or (month < 1)):
        return False

    # Validate day using previous days_in_month function
    if ((day > days_in_month(year, month)) or (day < 1)):
        return False

    # return True if not caught by any conditionals
    return True

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    # input validation using previous is_valid_date function
    if ((not is_valid_date(year1, month1, day1)) or
            (not is_valid_date(year2, month2, day2))):
        return 0

    # turn both dates into date objects using datetime module
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    # validate that date1 comes before date2
    if date1 > date2:
        return 0

    # subtract date1 from date2 to find the delta
    date_delta = date2 - date1

    #return days
    return date_delta.days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    # input validation using previous is_valid function
    if not is_valid_date(year, month, day):
        return 0

    birth_date = datetime.date(year, month, day)
    todays_date = datetime.date.today()

    # check to make sure birthday does not come after today's date
    if birth_date > todays_date:
        return 0

    # core logic - find delta of both dates and return days
    return (todays_date - birth_date).days
