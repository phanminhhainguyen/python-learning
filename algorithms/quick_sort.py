def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    
    left = []
    equal = []
    right = []
    for i in array:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            right.append(i)
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    return sorted_left + equal + sorted_right