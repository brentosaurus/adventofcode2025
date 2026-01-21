#-------------------------------------------------------------
# Advent of Code 2025
#-------------------------------------------------------------
import time

#-------------------------------------------------------------
MIN_DAY = 1
MAX_DAY = 25
codes = [None] * (MAX_DAY + 1)
times = [0] * (MAX_DAY + 1)

print('================ loading files ================')
for day in range(MIN_DAY, MAX_DAY + 1):
	filename = f'day{day}.py'
	try:
		with open(filename) as f:
			codes[day] = compile(f.read(), filename, 'exec')
	except FileNotFoundError:
		pass

for day in range(MIN_DAY, MAX_DAY + 1):
	startTime = time.time()
	if codes[day]:
		print('================ day', day, '================')
		exec(codes[day], None, None)
		times[day] = time.time() - startTime

print('================ times ================')
for day in range(MIN_DAY, MAX_DAY + 1):
	if codes[day]:
		print('day', day, '=', round(times[day], 2), 'seconds')
print('================ total time', round(sum(times), 1), 'seconds ================')