from special_number import find_special_numbers, list_of_main_numbers

special_list = find_special_numbers(list_of_main_numbers)

def special_integer_to_roman(num):
    roman_dict_number = {
        999 : 'IM',
        995 : 'VM',
        990 : 'XM',
        950 : 'LM',
        900 : 'CM',
        499 : 'ID',
        495 : 'VD',
        490 : 'XD',
        450 : 'LD',
        400 : 'CD',
        99 : 'IC',
        95 : 'VC',
        90 : 'XC',
        49 : 'IL',
        45 : 'VL',
        40 : 'XL',
        9 : 'IX',
        4 : 'IV',
    }
    
    return roman_dict_number[num]


def integer_to_roman(components_of_numbers : list[int]) -> str:
    
    roman_dict_number = {
        1000 : 'M',
        500 : 'D',
        100 : 'C',
        50 : 'L',
        10 : 'X',
        5 : 'V',
        1 : 'I'
    }

    my_number = ""
   
    for int_number in components_of_numbers:
        for roman_number in roman_dict_number:
            if int_number in special_list:
                value = special_integer_to_roman(int_number)
                my_number += value
                break
            
            else:
                if int_number % roman_number == 0: 
                    value = int_number // roman_number
                    my_number += roman_dict_number[roman_number] * value
                    break
                   
    return my_number

    