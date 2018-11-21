def arraytoInt(list):
	result = str()
	for x in list:
		result+=str(x)
	return result

print(arraytoInt([1,2,3]))