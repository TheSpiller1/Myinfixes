import stack_list
stack = stack_list.ShankarStack()
restack = []
while True:
    element = input("Please input your symbol: ")
    if element == 'quit':
        break
    stack.push(element)
for every_num in range(stack.size):
    restack.append(stack.peeking())
    stack.pop()

print(restack)


