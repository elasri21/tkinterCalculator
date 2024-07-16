import tkinter as tk

# create main window
root = tk.Tk()
root.title("Calculator")

# entry widget for display
display = tk.Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

ops = ['+', '-', '*', '/']


# check if an insert is valid
def is_valid_insert(old, new):
    if len(old) > 0 and new == '.':
        for char in old:
            if char in ops and old.index(char) == len(old) - 1:
                return False
    return True


# check for this format 12.45.
def valid_number(old, new):
    if len(old) > 0 and new == '.':
        for i in range(len(old) - 1, 0, -1):
            if old[i] in ops:
                return True
            if old[i] == '.':
                return False
    return True


# is operation in number
def not_has_op(curr, new):
    if new == '.':
        return False
    for op in ops:
        if op in curr:
            return False
    return True


# Button click function
def button_click(number):
    current = display.get()
    # prevent insert multiple .
    # if len(current) > 0 and current[len(current) - 1] == '.' and number == '.':
    #     return
    # if len(current) > 0 and current[len(current) - 1] in ops and number == '.':
    #     return
    if not is_valid_insert(current, number) or not valid_number(current, number):
        return
    if len(current) == 0 and (number in ops or number in [')', '.']):
        return

    # if allow to change operation at the same place
    for op in ops:
        if op in current and number in ops:
            if current[len(current) - 1] in ops:
                current = current[0:-1]

    display.delete(0, tk.END)
    display.insert(0, current + str(number))


# button decimal
def button_decimal(number):
    current = display.get()
    no_op = True
    if number == ".":
        if (len(current) == 0) or (len(current) > 0 and current[len(current) - 1] == "."):
            return
        for c in current:
            if c in ops:
                no_op = False
                break
        if no_op and "." in current:
            return
        if len(current) > 0 and current[len(current) - 1] in ops:
            return
        if not valid_number(current, number):
            return
    display.delete(0, tk.END)
    display.insert(0, current + str(number))


# parentheses
def button_parentheses(number):
    curr = display.get()
    if number == ")" and "(" not in curr:
        return
    display.delete(0, tk.END)
    display.insert(0, curr + str(number))


# button clear function
def button_clear():
    display.delete(0, tk.END)


# delete
def button_delete():
    curr = display.get()
    if len(curr) > 0:
        display.delete(len(curr) - 1, tk.END)


# button equal function
def button_equal():
    if len(display.get()) == 0:
        return 
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except ZeroDivisionError as err:
        display.delete(0, tk.END)
        display.insert(0, str(err))
    except ValueError as err:
        display.delete(0, tk.END)
        display.insert(0, str(err))
    except TypeError as err:
        display.delete(0, tk.END)
        display.insert(0, str(err))
    except SyntaxError as err:
        display.delete(0, tk.END)
        display.insert(0, str(err))


# list of buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('←', 5, 3)
]

# add all buttons to the window
for (text, row, column) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal)
    elif text == "C":
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_clear)
    elif text == "←":
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_delete)
    elif text == ".":
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_decimal(t))
    elif text in ["(", ")"]:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_parentheses(t))
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column)

# main loop
root.mainloop()
