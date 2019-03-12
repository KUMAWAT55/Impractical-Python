def main():
    file = open('List_Algorithms.txt', "r")
    lines = list(file)
    for line in lines:
        print(line)
    file.close()
    algorithm_to_call = int(input("Enter the number from below list algorithms :"))
    if algorithm_to_call == 1:
        print("You Have Selected PrimeCheck")
        from prime_check_file import prime_check
        if prime_check(int(input("Enter a number to check Prime/Not Prime :"))):
            print("It is a Prime Number")
        else:
            print("Not a Prime Number!")
if __name__ == '__main__':
    main()
