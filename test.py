user_input = 'a+b*c+d'
new_input = ""
if "(" in user_input:
    for every_ex in user_input:
        if every_ex == '(':
            while every_ex == ')':
                new_input += every_ex
m_d_counter = 0
for every_ex in user_input:
    if every_ex == '/':
        new_input += (user_input[m_d_counter - 1] + every_ex + user_input[m_d_counter + 1])
    elif every_ex == '*':
        new_input += (user_input[m_d_counter - 1] + every_ex + user_input[m_d_counter + 1])

    m_d_counter += 1
a_s_counter = 0
for every_ex in user_input:
    if every_ex == '+':
        new_input += (user_input[a_s_counter - 1] + every_ex + user_input[a_s_counter + 1])
    if every_ex == '-':
        new_input += (user_input[m_d_counter - 1] + every_ex + user_input[m_d_counter + 1])
    a_s_counter += 1
print(new_input)
