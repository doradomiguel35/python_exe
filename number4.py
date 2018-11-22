def array_to_Int(list):
	result = str()
	for x in list:
		result+=str(x)
	return result

print(array_to_Int([1,2,3]))