import tkinter as tk

from special_number import find_special_numbers, list_of_main_numbers
from components_of_number import find_component_number
from convert_number import *
from errors import ZeroNumberError, NegativeNumberError

root = tk.Tk()

result_var = tk.StringVar(master=root,)

int_number_lbl = tk.Label(
    master=root,
    text="Integer number: ",
    width=20,
    height=2,
)

int_number_lbl.grid(row=0, column=0, columnspan=1)

int_number_ent = tk.Entry(
    master=root,
    width=40,
)

int_number_ent.grid(row=0, column=1, columnspan=3)

roman_number_lbl = tk.Label(
    master=root,
    text="Roman number: ",
    width=20,
    height=3,
)

roman_number_lbl.grid(row=1, column=0, columnspan=1)

result_number_lbl = tk.Label(
    master=root,
    text="answer",
    width=40,
)

result_number_lbl.grid(row=1, column=1, columnspan=3)

def button_clicked(*args):
    special_list = find_special_numbers(list_of_main_numbers)
    result_var = int_number_ent.get()
    try:
        answer = int(result_var)
        if answer == 0:
            raise ZeroNumberError
        
        elif answer < 0:
            raise NegativeNumberError
        
        components_of_numbers = find_component_number(answer, special_list)
        result_number_lbl["text"] = integer_to_roman(components_of_numbers)

    except ValueError:
        result_number_lbl['text'] = "You must enter and integer number"

    except ZeroNumberError:
        result_number_lbl['text'] = "Invalid number"
        
    except NegativeNumberError:
        result_number_lbl['text'] = "You must enter a positive number"
    
change_number_btn = tk.Button(
    master=root,
    text="Change",
    fg="blue",
    command=button_clicked,
)

change_number_btn.grid(row=0, column=5, columnspan=5)
root.bind("<Return>", button_clicked)

quit_number_btn = tk.Button(
    master=root,
    text="Quit",
    fg="red",
    command=quit,
)

quit_number_btn.grid(row=1, column=5, columnspan=5)
root.bind("<q>", quit)

root.mainloop()