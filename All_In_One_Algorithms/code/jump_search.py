'''Jump Search algorithm code'''
def jump_search(elements, item, first, interval, count):
    '''Function Implemented
    ----------------------------------------------
    Complexity Terms
    ----------------------------------------------
    Worst case time complexity:     O(√N)
    Average case time complexity:   O(√N)
    Best case time complexity:      O(1)
    Space complexity:               O(1)'''
    for i in range(first, len(elements), interval):
        if elements[i] < item:
            count = count+1
            first = i
        elif elements[i] == item:
            count = count+1
            return "Found at Index : {} \nTotal Number of steps : {}".format(i, count)
        else:
            break
    index = first
    for j in elements[first:]:
        if j == item:
            count = count+1
            return "Found at Index : {} \nTotal Number of steps : {}".format(index, count)
        index = index+1
    return "Not Found !!"
