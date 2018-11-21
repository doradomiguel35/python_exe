def dictGroup(group,lists):
	dictionary = dict()
	for x in range(len(group)):
		for y in range(len(lists)):
			print(lists[y])
			dictionary[group[x]] = lists[y]
			lists.pop(y)
			break
	return dictionary 


print(dictGroup(["A","B"],[['Jay','Anna'],['Kim','Kc']]))