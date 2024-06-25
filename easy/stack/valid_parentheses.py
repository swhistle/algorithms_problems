def is_valid_parentheses(s: str) -> bool:
    parentheses_stack = []

    open_parentheses_set = set(['(', '[', '{'])
    close_parentheses_set = set([')', ']', '}'])

    for char in s:
        if char in open_parentheses_set:
            parentheses_stack.append(char)
        elif char in close_parentheses_set and len(parentheses_stack) > 0:
            last_open_parenthesis = parentheses_stack.pop()

            if char == ')' and last_open_parenthesis == '(':
                continue
            elif char == ']' and last_open_parenthesis == '[':
                continue
            elif char == '}' and last_open_parenthesis == '{':
                continue
            else:
                return False
        else:
            return False

    return len(parentheses_stack) == 0


str_1 = ''
res_1 = is_valid_parentheses(str_1)
print(res_1)

str_2 = '()'
res_2 = is_valid_parentheses(str_2)
print(res_2)

str_3 = '()[]{}'
res_3 = is_valid_parentheses(str_3)
print(res_3)

str_4 = '(]'
res_4 = is_valid_parentheses(str_4)
print(res_4)