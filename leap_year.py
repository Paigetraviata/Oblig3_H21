
def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        #print("year is leap year")
        return True

    if (year % 100 == 0) and (year % 400 != 0) or (year % 4 != 0):
        #print ("year is not leap year")
        return False

print(is_leap_year(0000))




