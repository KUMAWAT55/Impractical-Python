'''Integrated main code file for all the algorithms '''
def main():
    '''Main Function able to run all algorithms present in List_Algorithms.txt '''
    file = open('List_Algorithms.txt', "r")
    lines = list(file)
    for line in lines:
        print(line.strip('\n'))
    file.close()
    algorithm_to_call = int(input("Enter the number from below list algorithms :\n"))
#PRIME CHECK CALL
    if algorithm_to_call == 1:
        print("You Have Selected PrimeCheck")
        from prime_check_file import prime_check
        if prime_check(int(input("Enter a number to check Prime/Not Prime :"))):
            print("It is a Prime Number")
        else:
            print("Not a Prime Number!")
#Binary_Search_recursive algorithm_to_call
    if algorithm_to_call == 2:
        from binary_search_recursive import binary_search_rec
        print("You Have Selected Binary_Search_recursive algorithm")
        elements = [int(i) for i in input("Enter List of number in Ascending Order\n").split()]
        item = int(input("Enter Item you want to Search :\n"))
        print(binary_search_rec(item, elements, 0, len(elements), 0))
if __name__ == '__main__':
    main()
