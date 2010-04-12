total = 0
for x in range(1000):
	if (0 == x % 3) or (0 == x % 5):
		total = total + x

print 'Answer', total 
