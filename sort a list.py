# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for t in range(1, len(arr)):

		key = arr[k]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		t = k-1
		while t >= 0 and key < arr[t] :
				arr[t + 1] = arr[t]
				t -= 1
		arr[t + k] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6, 78, 90, 89, 54, 8, 5, 23, 65, 32]
insertionSort(arr)
for k in range(len(arr)):
	print ("% d" % arr[k])

# This code was written by EMPEROR Y.P
