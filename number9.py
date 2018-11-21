def unique(list):
	for x in list:
		if x in list:
			list.remove(x)
	print(list)
#Not yet Done
unique([1,2,3,1,3])
