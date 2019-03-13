'''Linear Search algorithm code'''
def linear_search(elements, item):
    '''Function Implemented
        ----------------------------------------------
        Complexity Terms
        ----------------------------------------------
        Worst-case space complexity:    O(1)
        Best-case performance:          O(1)
        Worst-case performance:         O(n)'''
    for i, element in enumerate(elements):
        if element == item:
            return "Found at Index : {}".format(i)
    return "Item Not Present !!!"
