def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2
    if left < n and arr[i] < arr[left]: # See if left child of root exists and is greater than root
        largest = left

    if right < n and arr[largest] < arr[right]: # See if right child of root exists and is greater than root
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest) # Heapify the root.

def heapSort(arr):
    n = len(arr)

    # Build a maxheap. 
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

## Test list
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Sorted array is:", arr)