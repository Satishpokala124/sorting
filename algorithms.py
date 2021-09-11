
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j] = arr[j] + arr[j+1]
				arr[j+1] = arr[j] - arr[j+1]
				arr[j] = arr[j] - arr[j+1]
	return arr

def merge(arr1, arr2):
	arr = []
	i = 0; j = 0
	n1 = len(arr1); n2 = len(arr2)
	while i<n1 and j<n2:
	 	if arr1[i]<arr2[j]:
	 		arr.append(arr1[i])
	 		i+=1
	 	else :
	 		arr.append(arr2[j])
	 		j+=1
	while i<n1:
		arr.append(arr1[i])
		i+=1
	while j<n2:
		arr.append(arr2[j])
		j+=1
	return arr

def mergeSort(arr):
	if len(arr)==1:
		return arr 
	middle = len(arr)//2
	arr1 = arr[:middle]
	arr2 = arr[middle:]
	arr1 = mergeSort(arr1)
	arr2 = mergeSort(arr2)
	arr = merge(arr1, arr2)
	return arr