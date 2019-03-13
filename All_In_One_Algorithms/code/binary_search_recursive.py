'''Binary Search algorithm code'''
def binary_search_rec(item, elements, first, last, count):
    '''Function Implemented in recursive manner
        ----------------------------------------------
        Complexity Terms
        ----------------------------------------------
        Worst-case performance	     O(log n)
        Best-case performance	     O(1)
        Average performance          O(log n)
        Worst-case space complexity  O(1)'''
    if last > first:
        count = count+1
        mid = int((first+(last-1))/2)
        if elements[mid] == item:
            return "Found at Index : {} \nTotal Number of iterations : {}".format(mid, count)
        elif elements[mid] > item:
            return binary_search_rec(item, elements, first, mid-1, count)
        return binary_search_rec(item, elements, mid+1, last, count)
    return "Item Not Present !!!"
