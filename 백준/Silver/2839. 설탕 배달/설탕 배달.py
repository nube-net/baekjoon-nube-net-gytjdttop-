n = int(input())
n1 =0
a5 = n//5
a3 = n//3
key = 0
key1 = 0
result3 = 99999
result5 = 99999

for i in range(int( a5), -1,-1) :
	n1 = n
	n1 -= int(5*i)
	if n1%3 == 0 :
		result5 = int(i + int(n1//3))
		key = 1
		break

for i in range(int( a3), -1,-1) :
	n1 = n
	n1-= int(3*i)
	if n1%5 == 0 :
		result3 = int(i + int(n1//5))
		key1 =1
		break

if key == 0 and key1 == 0 :
	print(-1)
else :
	if result3 > result5 :
		print(result5)
	elif result5 > result3 :
		print(result3)
	else :
		print(result3)
