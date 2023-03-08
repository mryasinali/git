def sorter_handler(list):
    try:
        #using python 3.11
        #set removes any duplicates in the array
        #sorted orders the list, reverse sorts it in decending order
        all(isinstance(x, int) for x in list)
        sorted_list = sorted(set(list), reverse=True)
        print(sorted_list)
        return sorted_list
    except TypeError as e:
        print(f"Please enter values as a list of integers. e.g. 1 2 3 : {e}")
    except Exception as e:
        print(f"An exception occurred: {e}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = input().split()
    input_int_array = [int(x) for x in list]
    # input list as numbers with spaces only
    # list is adjusted above, have not implemented command line input with input()
    # list can be any length, sorting is not constrained to positive integers
    # list is not constrained to only 4 duplicates
    # input is provided as an array
    sorter_handler(input_int_array)
