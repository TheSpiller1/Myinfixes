import stack_list


def change(postfix_input):
    stack = stack_list.ShankarStack()
    operators = ["*", "/", "+", "-", "^"]
    for every_expression in postfix_input:
        if every_expression not in operators:
            stack.push(every_expression)
        else:
            new_push = ""
            new_push += every_expression
            a = stack.peek.get_data()
            stack.pop()
            b = stack.peek.get_data()
            new_push += b
            new_push += a
            stack.pop()
            stack.push(new_push)
    output = ""
    output += stack.peek.get_data()
    return output


def inputer():
    swap_item = input("Please input a algebraic expression: ")
    return swap_item


print(change(inputer()))


