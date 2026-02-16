def sum_array(arr):
    biggest = 0
    smallest = 0
    for item in arr:
        if item > biggest:
            biggest = arr[i]
        elif item < biggest:
            smallest = item
            
    for item in arr:
        if item < smallest:
            smallest = item
            
    arr.remove(biggest)
    arr.remove(smallest)
    
    return sum(arr)

print(sum_array([1, 2, 3, 4, 5]))