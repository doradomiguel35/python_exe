def display_unique(lists):
	for x in range(len(lists)):
		for y in range(len(lists)):
			if x == y:
				print(str(x)+" "+str(y))
				print(range(len(lists)))
		lists.remove(lists[x])	
#Not yet Done
display_unique([1,2,3,1,3])
