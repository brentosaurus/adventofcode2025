#-------------------------------------------------------------
# Advent of Code 2025
# This might be optimized by checking the smallest repeat lengths
# first, and knowing that if there's no repeat with length N,
# there can't be one with length N * 2, etc.
# But the numbers are so short that it shouldn't make much difference.
# A better optimization would reduce the number of integers checked,
# by skipping those that can't possibly have repeats. Not sure how...
#-------------------------------------------------------------
import parse

testData = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""".split('\n')

data = """\
824-1475,967620-1012917,2727216511-2727316897,56345-141494,8811120-8999774,5727326-5922513,935306-961989,76751455-76787170,723458-849157,144648-162230,1597-3207,326085-472746,14-34,66-132,9453977670-9454023729,959903262-960027272,17168-26699,190-332,3351-5602,1-11,371280315-371448887,6252062-6312899,9696887156-9697040132,37-58,32770-52161,6443650762-6443689882,473092-582157,3309726-3347079,852735-912990,8294840594-8294926063,3773964-3884030,7718304-7809359,601947-677833,3434304207-3434405118,449-673,64525269-64702774,31545468-31784543,184451-308951,5771-11485\
""".split('\n')
	
#-------------------------------------------------------------
def go(lines, part):
	result = 0

	def repeating(s, n):
		if len(s) % n != 0:
			return False
		i = len(s) // n
		return all(s[0:i] == s[i * j:i * j + i] for j in range(1, n))

	ranges = lines[0].split(',')
	for r in ranges:
		#print('    ', r)
		a,b = map(int, r.split('-'))
		for i in range(a, b + 1):
			s = str(i)
			if part == 1:
				if repeating(s, 2):
					result += i
					#print(i, 'contains repeat with factor', 2)
			else:
				for j in range(2, len(s) + 1):
					if repeating(s, j):
						#print(i, 'contains repeat with factor', j)
						result += i
						break

	print(result)
	return result

#-------------------------------------------------------------
assert(go(testData, 1) == 1227775554)
assert(go(data, 1) == 52316131093)
assert(go(testData, 2) == 4174379265)
assert(go(data, 2) == 69564213293)