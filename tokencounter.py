from tkinter import Tk, Frame, TOP, Label, Entry, Button
def count_token(_list):
    count = 0
    for val in _list:
        if type(val) is list:
            count += 2
            count += count_token(val)
        else:
            count += 1
    return count
def validate_expr(_input, target=0, awaiting_operand=False, is_inside_group=False, group_first_val=True):
    expr_list = []
    loop_error = 0
    while target < len(_input):
        if (_input[target] is "(") and (target != (len(_input)-1)):
            _ = validate_expr(_input, target=target+1, is_inside_group=True) 
            if isinstance(_, tuple):
                sub_list, target = _
                expr_list.append(sub_list)
                awaiting_operand = False
                group_first_val = False
            else:
                return _
        elif (_input[target] is ")") and (is_inside_group == True) and (awaiting_operand == False) and (group_first_val == False):
            return expr_list, target+1
        elif (_input[target] is "*") and (awaiting_operand == False) and (target != (len(_input)-1)) and (group_first_val == False):
            expr_list.append(_input[target])
            awaiting_operand = True
            group_first_val = False
            target += 1
        elif(_input[target] is "+") and (awaiting_operand == False) and (target != (len(_input)-1)):
            expr_list.append(_input[target])
            awaiting_operand = True
            group_first_val = False
            target += 1
        elif _input[target] is "a":
            expr_list.append(_input[target])
            awaiting_operand = False
            group_first_val = False
            target += 1
        else:
            loop_error = 1
            create_tk_error()
            break
    if loop_error == 0 and is_inside_group == True:
        return create_tk_error()
    elif loop_error == 0:
        return expr_list, target
def on_submit(_input):
    _list = []
    for char in _input:
        if char is not " ":
            if char is "{" or char is "(":
                _list.append("(")
            elif char is "}" or char is ")":
                _list.append(")")
            elif char is "*" or char is "/":
                _list.append("*")
            elif char is "+" or char is "-":
                _list.append("+")
            else:
                _list.append("a")
    _ = validate_expr(_list)
    if isinstance(_, tuple):
        _list, _ = _
        create_tk_result(count_token(_list))
def create_tk_error():
    error = Tk()
    error.wm_title("!")
    label = Label(error, text="Invalid expression.")
    label.pack(side="top")
    button = Button(error, text="Okay", command=error.destroy)
    button.pack(side="bottom")
    error.mainloop()
def create_tk_result(result):
    message = "The number of token in your input is {}.".format(result)
    result = Tk()
    result.wm_title("Count")
    label = Label(result, text=message)
    label.pack(side="top")
    button = Button(result, text="Okay", command=result.destroy)
    button.pack(side="bottom")
    result.mainloop()
def create_tk_app():
    root = Tk()
    root.wm_title("Token counter")
    main_frame = Frame(root)
    main_frame.pack(side=TOP)
    Label(main_frame, text="Enter a valid arithmetic expression:").grid(row=0)
    _input = Entry(main_frame)
    submit = Button(main_frame, command=lambda: on_submit(_input.get()), text="Submit", fg="darkgreen")
    _input.grid(row=1, column=0)
    submit.grid(row=1, column=1)
    root.mainloop()
create_tk_app()
# sample stupid inputs
# a(b) + -  }{}
# 3b(a) + 21 })+
# rare but valid input
# (a)(1+(b)) + a
# (3)(2)a + bca
# expression* operator expression*
# expression is an expression or variable or number
# expression determiner is if it starts with ( or {
# if expression, must start with ( and end with )
# variable is number with letters or letters only
# EXPRESSION IS...
# int*, str*, int*str*, (expr*), (expr* oper expr*)
# if int is targeted... must proceed with int*, str* or expr*
# if str is targeted... must proceed with int*, str* or expr* 
# if ({ is targeted... must proceed with int*, str* or expr* and end with })
# [[a, +, b], + [a, +, b]]
# input = (a+b)+(a)+a(a+b)
# count = 6
# main_list = [[a, +, b], +, []]
# targeted_list = main_list[2]




  
