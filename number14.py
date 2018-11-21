def removeNonInt(lists):
	for x in range(len(lists)):
		if type(lists[x]) != type(int()):
			lists.pop(x)
			break
	return lists

#Not yet Done
print(removeNonInt([2,'a','2', {1: 'one'}]))