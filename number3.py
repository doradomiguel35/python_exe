def get_Odd(lists):
	newList = list(())
	for x in lists:
		if x % 2 != 0:
			newList.append(x)
	return newList

print(get_Odd([1,2,3,4,5,6,7,8,9,10]))