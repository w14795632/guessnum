import random

r = random.randint(1, 100)
r = int(r)



while True:
	num = input("請猜一個數字: ")
	num = int(num)
	if num == r:
		print("恭喜你猜對了!!")
		break
	elif num > r :
		print('比答案小喔，在猜一次')

	elif num < r:

		print('比答案大喔，在猜一次')

		