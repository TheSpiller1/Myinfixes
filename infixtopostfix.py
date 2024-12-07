import stack_list


def swap(user_input):
    user_input = user_input.replace(" ", "")

    stack = stack_list.ShankarStack()
    precedence = {"+": 1,
                  "-": 1,
                  "*": 2,
                  "/": 2,
                  "^": 3,
                  "(": 0}
    postfix_expression = ""
    for every_operand_operator in user_input:
        if every_operand_operator in precedence:
            if stack.size < 1 or stack.checking("(") or every_operand_operator == "(":
                stack.push(every_operand_operator)

            elif precedence.get(stack.peek.get_data()) >= precedence.get(every_operand_operator):
                while precedence.get(stack.peek.get_data()) >= precedence.get(every_operand_operator):
                    postfix_expression += stack.peek.get_data()
                    stack.pop()
                    if stack.size < 1:
                        stack.push(every_operand_operator)
                        break
                if stack.size != 1:
                    stack.push(every_operand_operator)
            else:
                stack.push(every_operand_operator)

        elif every_operand_operator == ")":
            while stack.peek.get_data() != "(":
                postfix_expression += stack.peek.get_data()
                stack.pop()

            stack.pop()

        else:
            postfix_expression += every_operand_operator

    for every_num in range(stack.size):
        postfix_expression += stack.peek.get_data()
        stack.pop()

    return postfix_expression


swap_item = input("Please input a algebraic expression: ")

print(swap(swap_item))
