s = int(input())

b = 0
while s >= 0:
	if s%5 ==0:
		b += (s//5)
		print(b)
		break
	s -=3
	b +=1
else :
	print(-1)