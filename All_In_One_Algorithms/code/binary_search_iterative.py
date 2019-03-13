'''Binary Search algorithm code in iterative manner'''
def binary_search_iter(item, elements, first, last, count):
    '''Function Implemented in Iterative manner
        ----------------------------------------------
        Complexity Terms
        ----------------------------------------------
        Worst-case performance	     O(log n)
        Best-case performance	     O(1)
        Average performance          O(log n)
        Worst-case space complexity  O(1)'''
    print("[Iterative Binary search function called]")
    while last > first:
        count = count+1
        mid = int((first+(last-1))/2)
        if elements[mid] == item:
            return "Found at Index : {} \nTotal Number of iterations : {}".format(mid, count)
        elif elements[mid] > item:
            last = mid-1
        else:
            first = mid+1
    return "Item Not Present !!!"
