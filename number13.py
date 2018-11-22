def check_Difference(list1,list2):
	newList = list(())
	for x in list1:
		if x in list2:
			continue
		else:
			newList.append(x)
	return newList

print(check_Difference(list((1,2,3,4,5)),list((5,2,10))))