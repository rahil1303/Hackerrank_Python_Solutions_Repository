#Method 1
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
   
    # Write your logic here
    
    

year = int(input())
print(is_leap(year))


#Method 2
def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
	if (year % 400 == 0):
                leap = True
    return leap
  
  #Method 3
  import calendar

def is_leap(year):
    return calendar.isleap(year)
