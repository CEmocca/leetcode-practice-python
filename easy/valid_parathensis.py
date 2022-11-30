class ValidParatheses:
    def __init__(self) -> None:
        pass

    # first try
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if(len(stack) == 0):
                stack.append(char)
            else:
                prev = stack.pop()
                if(prev == '(' and char == ')'):
                    continue
                elif(prev == '{' and char == '}'):
                    continue
                elif(prev == '[' and char == ']'):
                    continue
                else:
                    stack.append(prev)
                    stack.append(char)
        return len(stack) == 0

    # idea is to check that char is in values of dictionary. If so then we can check the latest char inside stack is the key of current char
    def is_valid_top_vote(self, s: str) -> bool:
        stack = []
        p_dict = dict([('}', '{'), (']', '['), (')', '(')])
        for char in s:
            if char in p_dict.values():  # always put close parathensis into stack
                stack.append(char)
            elif char in p_dict.keys():  # if char is in keys, which mean that it need open parathensis to match
                if len(stack) == 0 or p_dict[char] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0



def main():
    solution = ValidParatheses()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.is_valid_top_vote("()"))
    print(solution.is_valid_top_vote("()[]{}"))
    print(solution.is_valid_top_vote("(]"))

main()