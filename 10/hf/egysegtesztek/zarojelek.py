def helyeszarojel(s):
    zarojelparok = {"(": ")", "{": "}", "[": "]"}

    stack = []

    for char in s:
        if char in zarojelparok.values():
            # If we encounter a closing parenthesis, check if it matches the top of the stack
            if not stack or zarojelparok[stack.pop()] != char:
                return False
        elif char in zarojelparok:
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)

    return len(stack) == 0
