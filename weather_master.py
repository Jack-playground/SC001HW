"""
File: weather_master.py
Name:Shawn
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

exitCode = -1


def main():
	"""
	TODO:
	"""
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input('Next Temperature: (or ' + str(exitCode) + ' to quit)? '))
	max_temperature = temperature
	min_temperature = temperature
	days = 1
	count_cold_days = 0
	total = temperature
	if is_cold_day(temperature):
		count_cold_days += 1
	while True:
		temperature = int(input('Next Temperature: (or ' + str(exitCode) + ' to quit)? '))
		if temperature == exitCode:
			break
		elif is_max(temperature, max_temperature):
			max_temperature = temperature
		elif is_min(temperature, max_temperature):
			min_temperature = temperature
		if is_cold_day(temperature):
			count_cold_days += 1
		total += temperature
		days += 1

	print('Highest Temperature = '+str(max_temperature))
	print('Lowest Temperature = ' + str(min_temperature))
	print('Average = '+str(total/days))
	print(str(count_cold_days)+' cold day(s)')


def is_cold_day(temperature):
	return temperature < 16


def is_max(temperature, max_t):
	return temperature > max_t


def is_min(temperature, min_t):
	return temperature > min_t


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
