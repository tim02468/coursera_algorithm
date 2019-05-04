# implement Karatsuba Algorithm
def karatsuba(x, y):

	strX = str(x)
	strY = str(y)
	multi_val = 1

	# deal with unequal size
	if len(strX) != len(strY):
		maxLength = max(len(strX), len(strY))
		minLength = min(len(strX), len(strY))

		multi_val = 10 ** (maxLength - minLength)

		if len(strX) == minLength:
			strX = str(x * multi_val)
		else:
			strY = str(y * multi_val)

	# base case
	if len(strX) < 4 or len(strY) < 4:
		return x * y
	
	a = strX[:int(len(strX) / 2)]
	b = strX[int(len(strX) / 2):]
	c = strY[:int(len(strY) / 2)]
	d = strY[int(len(strY) / 2):]
	
	n = len(b)

	step1 = karatsuba(int(a), int(c))
	step2 = karatsuba(int(b), int(d))
	step4 = karatsuba(int(a), int(d)) + karatsuba(int(b), int(c))
	out = 10 ** (2*n) * step1 + 10 ** n * step4 + step2		

	return out / multi_val

# test
x = 313123132
y = 23422

out = karatsuba(x, y)
print(out)
