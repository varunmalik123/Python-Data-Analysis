import calendar

def number_of_days(year,month):

	"""
	The purpose of this function is to return the number of days in a month given the month and the year 

	:param year(int): Input year
	:param month(int): Input month

	"""
	assert isinstance(year,int)
	assert isinstance(month,int)
	assert 1 <= month <= 12
	assert (year > 0 )

	month_packed = calendar.monthcalendar(year,month)

	month_unpacked = []

	for outer_list in month_packed:
		for days in outer_list:
			month_unpacked.append(days)

	return max(month_unpacked)


def number_of_leap_years(year1,year2):

	"""
	This function returns the number of leap years between year1 and year 2 inclusive

	:param year1 (int): Input start year
	:param year2 (int): Input end year

	"""
	assert isinstance(year1, int)
	assert isinstance(year2, int)
	assert (year2) >= (year1)
	assert (year1 > 0) and (year2 > 0)

	no_of_leap_years = calendar.leapdays(year1, year2+1) 

	return no_of_leap_years

def get_day_of_week(year,month,day):

	"""
	This function returns the day given the date

	:param year (int): Input year
	:param month (int): Input month 
	:param day (int): Input day
	"""
	assert isinstance(year, int)
	assert isinstance(month, int)
	assert isinstance(day, int)
	assert 1 <= month <= 12
	assert year > 0 
	assert 1 <= day <= number_of_days(year,month)
	#days = calendar.day_name
	day = calendar.weekday(year,month,day)
	
	return list(calendar.day_name)[day]



