import stack_list


def change(user_i):
    stack = stack_list.ShankarStack()
    output = ""
    operators = {"+": 0,
                 "-": 0,
                 "*": 1,
                 "/": 1,
                 "(": 2}

    for every_expression in user_i:
        if every_expression in operators.keys():
            count = 0
            if stack.size > 1:
                if every_expression != ")":
                    if every_expression != "(":
                        while operators.get(every_expression) <= operators.get(stack.peek.get_data()):
                            if stack.size <= 1:
                                break
                            output += stack.peek.get_data()
                            stack.pop()
                            if count == 0:
                                stack.push(every_expression)
                            count += 1

                        else:
                            stack.push(every_expression)
                    else:
                        stack.push(every_expression)
                else:
                    input_a = ""
                    while stack.peek.get_data == "(":
                        input_a += stack.peek.get_data()
                        stack.pop()
                    o = change(input_a)
                    output += o

            else:
                stack.push(every_expression)

        else:
            output += every_expression
    for a in range(stack.size):
        output += stack.peek.get_data()
        stack.pop()

    output = output.replace("(", "")
    output = output.replace(")", "")

    return output


print(change("((A+B)–C*(D/E))+F"))
