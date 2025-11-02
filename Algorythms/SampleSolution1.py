import time

def bin_to_prime(lst, n):
    #developed by James
    list_of_num = []
    flag = False

    # Checks if the entered string is a binary value by checking each individual value to see if it is a 1 or 0
    while flag == False:
        for x in range(0, len(lst)):
            if lst[x] != '1' and lst[x] != '0' or lst == []:
                print("Invalid input")
                flag = False
                break
            else:
                flag = True
        if flag == False:
            lst = list(input("Enter value"))

    # cycles the list concatenating characters together into new strings
    for x in range(0, len(lst)):
        for y in range(x, len(lst)):
            if x == y:
                new_str = lst[x]
                deanery = int(new_str, 2)
                # removes duplicate data
                if deanery not in list_of_num and deanery <= int(n) and is_prime(deanery) == True:
                    list_of_num.append(deanery)
            else:
                new_str += lst[y]
                deanery = int(new_str, 2)
                if deanery not in list_of_num and deanery <= int(n) and is_prime(deanery) == True:
                    list_of_num.append(deanery)
    return return_lst(list_of_num)


def is_prime(num):
    #developed by Zanith
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def return_lst(lst):
    #Developed by James with inspiration from an algorithm made by Derrick Sherrill on www.youtube.com released on 9th september 2019
    def quicksort(lst):
        less_than = []
        greater_than = []
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst.pop()
        for x in range(0, len(lst)):
            if lst[x] > pivot:
                greater_than.append(lst[x])
            else:
                less_than.append(lst[x])
        lst = quicksort(less_than) + [pivot] + quicksort(greater_than)
        return lst
    lst = quicksort(lst)
    #developed by Zanith
    if len(lst) <= 6:
        return f"{', '.join(map(str, lst))}"
    else:
        return f"{', '.join(map(str, lst[:3] + lst[-3:]))}"

def timer(num, n):
    start = time.time()
    print(bin_to_prime(num, n))
    end = time.time()
    print("Time:", end-start)

print("START")
print("1")
timer("0100001101001111","999999")
print("2")
timer("01000011010011110100110101010000","999999")
print("3")
timer("1111111111111111111111111111111111111111","999999")
print("4")
timer("010000110100111101001101010100000011000100111000","999999999")
print("5")
timer("01000011010011110100110101010000001100010011100000110001", "123456789012")
print("6")
timer("0100001101001111010011010101000000110001001110000011000100111001","123456789012345")
print("7")
timer("010000110100111101001101010100000011000100111000001100010011100100100001","123456789012345678")
print("8")
timer("01000011010011110100110101010000001100010011100000110001001110010010000101000001","1234567890123456789")
print("9")
timer("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100","1234567890123456789")
print("10")
timer("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", "12345678901234567890")
#handwritten start
print("hand written test cases START")
# timer("1001", "9999999")
# timer("10110", "9999999999")
# timer("110101", "999999999")
# timer("0110110", "99999999")
# timer("11010011", "99999999")
print("END")

#Derrick Sherrill's quicksort video - https://www.youtube.com/watch?v=kFeXwkgnQ9U


