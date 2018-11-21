def find_index(lists,value):
	for x in range(len(lists)):
		if value == lists[x]:
			result = x
	return result

print(find_index(list((1,3,4)),4))