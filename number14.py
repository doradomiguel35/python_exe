def remove_non_int(lists):
	newList = []
	for x in lists:
		if type(x) != type(int()) :
			lists.remove(x)
		else:
			newList.append(x)
	return newList

print(remove_non_int([2,'a','2', {1: 'one'}]))