#-------------------------------------------------------------
# Advent of Code 2024
#-------------------------------------------------------------
import time

#-------------------------------------------------------------
DAYS = 25
codes = [None] * DAYS
times = [0] * DAYS

print('================ loading files ================')
for day in range(DAYS):
	filename = f'day{day + 1}.py'
	try:
		with open(filename) as f:
			print(day + 1)
			code = compile(f.read(), filename, 'exec')
			codes[day] = code
	except FileNotFoundError:
		pass

for day in range(DAYS):
	startTime = time.time()
	if codes[day]:
		print('================ day', day + 1, '================')
		exec(codes[day], None, None)
		times[day] = time.time() - startTime

print('================ times ================')
for day in range(DAYS):
	if codes[day]:
		print('day', day + 1, '=', round(times[day], 2), 'seconds')
print('================ total time', round(sum(times), 1), 'seconds ================')