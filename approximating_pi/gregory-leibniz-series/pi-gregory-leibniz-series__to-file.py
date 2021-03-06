# pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

MAX = 10**6

file = open("gregory-leibniz-series_10^6.txt","w")

pi = 4.0
divisor = 1
sign = 1

for i in range(1,MAX+1):
	sign *= -1
	divisor += 2
	pi += sign*(4.0/divisor)

	file.write(str(pi)+"\n")

file.close()
