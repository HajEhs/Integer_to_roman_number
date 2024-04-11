from special_number import list_of_main_numbers

def find_component_number(user_input : int, special_numbers : list[int]) ->list[int]:
    number_component = [] # includes the tuples of numbers
    
    final_number_component_list = [] # includes the numbers
    
    if user_input in special_numbers: # [4, 9, 40, 45, .....]
        final_number_component_list.append(user_input)
        return final_number_component_list

    for pointer in list_of_main_numbers: # [1000, 500, 100, 50, 10, 5, 1]
        result = user_input // pointer
        if result != 0:
            number_component.append((pointer, result)) # finding patch of numbers in user's input.
        user_input -= pointer * result    

    index = 0
    while True:
        if len(number_component) == 1:
            result = number_component[0][0] * number_component[0][1]
            final_number_component_list.append(result)
            return final_number_component_list
        
        try:
            number_first = number_component[index][0] * number_component[index][1]
            number_second = number_component[index + 1][0] * number_component[index + 1][1]
            result = number_first + number_second
            if result in special_numbers:
                final_number_component_list.append(result)
                index += 2
                if index >= len(number_component): # preventing infinity loop
                    return final_number_component_list
            else:
                final_number_component_list.append(number_first)
                index += 1

        except IndexError: # last index
                number_first = number_component[-1][0] * number_component[-1][1]
                number_second = number_component[-2][0] * number_component[-2][1]
                result = number_first + number_second
                if result not in special_numbers:
                    final_number_component_list.append(number_first)
                    return final_number_component_list
            
