import itertools


def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

    # Extract lst[i] or m from the list. remLst is
    # remaining list
    remLst = lst[:i] + lst[i+1:]
    # Generating all permutations where m is first
    # element
    for p in permutation(remLst):
        l.append([m] + p)
    return l


def all_combos(some_list):
    return itertools.permutations(some_list, len(some_list))


def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)

    # if end >= start:
    #     mid = (start + end) // 2
    #     if element == array[mid]:
    #         return mid
    #     if element < array[mid]:
    #         return binary_search(array, element, start, mid-1)
    #     else:
    #         return binary_search(array, element, mid+1, end)
    # else:
    #     return -1






knowns = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 14),
    (5, 42),
    (6, 132),
    (7, 429),
    (8, 1430)
]

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)


for i in range(18):
    integer_ratio = []
    index_found_at = []
    if 0 < i < 6:
        wee = [n + 1 for n in range(i)]
        combos = all_combos(wee)
        save_me_combo_kun = []
        count = 0
        for each in combos:

            save_me_combo_kun.append(each)
        #print("*"*100)
        #
        # x = (knowns[i][1]/(factorial(i)))
        # x = x.as_integer_ratio()
        # integer_ratio.append(x)
        # print(i, count, integer_ratio[i])

        for each in save_me_combo_kun:

            #print(each)
            # Test array
            arr = [1, 2, 3, 4, 5]
            x = 5

            # Function call
            result = binary_search(arr, x, 0, len(arr) - 1)
            if result != -1:
                #print("Element is at ", str(result))
                pass
            else:
                pass
                #print("Element not found")

            # run binary search on each permutation

            # need to sort list first
            #print(f"I am each: {each}")
            to_list = list(each)
            if len(to_list) > 1:
                pass
                #to_list.sort()
            #print(f"I am list: {to_list}")
            position_found_at = binary_search(to_list, i, 0, len(each) - 1)


            # append index into list for each length of array
            if position_found_at == -1:
                if i == to_list[0]:
                    #print(f"looks like {i} was at the first entry in {to_list}")
                    position_found_at = 0
                else:
                    pass

            if position_found_at == -1:
                print(f"this is the permutation{to_list} and this is the search term {i} and it was not found")
            else:
                print(f"this is the permutation{to_list} and this is the search term {i} and it was found at {position_found_at}")
            index_found_at.append(position_found_at)
