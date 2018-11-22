def find_Object(lists,properties):
	find = properties['index']
	result = set(())
	for x in lists:
		if find == x['index']:
			result = x

	return result

mylist = [{1:'one','index':0},{2:'two','index':1},{3:'three','index': 2}]
print(find_Object(mylist,{'index': 2}))

