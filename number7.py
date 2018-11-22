def array_To_Dict(list1,list2):
	dictionary = dict()
	for x in range(len(list1)):
		for y in range(len(list2)):
			dictionary[list1[x]] = list2[y]
			list2.pop(y)
			break
	return dictionary



print(array_To_Dict(['moe','larry','curly'],[30,40,50]))