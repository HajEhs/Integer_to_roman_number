list_of_main_numbers = [1000, 500, 100, 50, 10, 5, 1]

def find_special_numbers(list_of_number : list[int]) -> list:
    
    special_number = [] # [999, 995, 990, 950, 900 ,.....]

    len_list = len(list_of_number)

    for num_first in range(len_list - 1):
        for num_second in range(num_first + 1, len_list):
            value = list_of_number[num_first] - list_of_number[num_second]
            if value not in list_of_number:
                special_number.append(value)
                    
    special_number.sort(reverse=True) # [4, 9, 40, 45,.....]
    return special_number

