def display_unique(lists):
	newList = []
	for x in lists:
		if x in lists:
			newList.append(x)
			lists.remove(x)
	for x in lists:
		if x in newList:
			lists.remove(x)
	return lists
print(display_unique([1,2,3,1,3]))
