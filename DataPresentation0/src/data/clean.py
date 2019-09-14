import numpy as np

def fix_age1stcode(years_):
    # - Age: `Age`-> `nAge`  change < 13, or > 80 to `NaN`
    if years_ == 'Younger than 5 years':
        return 4.5
    elif years_ == 'Older than 85':
        return 85.
    else:
        return years_
        
def fix_years_coding(years_):
    # - years coding, years experience: `YearsCode` -> `nYearsCode`, change "Less than 1 year" to 1/10000 and "More than 50" to 55.
    # - years pro:`YearsCodePro` -> `nYearsPro`
    # make these numeric in a sensible way
    if years_ == 'Less than 1 year':
        return 0.0001
    elif years_ == 'More than 50 years':
        return 55.
    else:
        return years_

def fix_age(years_):
    # - 1st Code: `Age1stCode` -> `nAgeCode` , change "Younger than 5 years" to 4.5 and "Older than 85" to 85.
    # make these numeric in a sensible way  exclude pre-teens and aged >84
    if years_ < 13:
        return np.NaN
    elif years_ > 84:
        return np.NaN
    else:
        return years_

# Convert Age to generation with 2019 as current time reference
def find_gen(age):
    """
    """
    if age <= 22:
        gen = 'GenZ'
        return gen
    elif age <= 38:
        gen = 'Millenial'
    elif age <= 54:
        gen = 'GenX'
    elif age <= 73:
        gen = 'Boomer'
    else:
        gen = 'Silent'
    return gen

def fix_workweekhours(hours_):
    # - workweek: `WorkWeekHrs` to require 4 hours off per day
    # hard ceiling on hours in a week (24*7)  lets throw out the ridiculous no sleep 24/7 scenarios
    if hours_ > 20*7:
        return np.NaN
    elif hours_ < 4:  # arbitrary minimum work time
        return np.NaN
    else:
        return hours_
