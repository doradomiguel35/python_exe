def remove_Duplicates(lists):
	for x in range(len(lists)):
		if lists[x] in lists :
			lists.pop(x)
			break
	return lists


#Not yet Done
print(remove_Duplicates([1,3,2,3,2,6,2]))