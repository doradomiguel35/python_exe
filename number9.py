def display_unique(list):
	for x in list:
		if x in list:
			list.pop(x)
			break
	print(list)
#Not yet Done
display_unique([1,2,3,1,3])
