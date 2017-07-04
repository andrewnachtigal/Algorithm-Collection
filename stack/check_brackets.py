"""
Input: one string S which consists of big and small latin letters, digits, punctuation marks and brackets from the set []{}().
Output: If the string in S uses brackets correctly, output “Success". Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket.
"""

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def main_programe(text):
    opening_brackets_stack = []
    mismatched_info = (False, "Success")

    for i, next in enumerate(text, 1):
        # open bracket
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))

        # close bracket
        elif next == ')' or next == ']' or next == '}':
            if opening_brackets_stack.__len__() == 0:
                mismatched_info = (True, i)
                break
            else:
                open_brack = opening_brackets_stack.pop()
                if open_brack.Match(next):
                    continue
                else:
                    mismatched_info = (True, i)
                    opening_brackets_stack = []
                    break
        else:
            pass
    if opening_brackets_stack.__len__() != 0:
        print (opening_brackets_stack[0].position)
    elif mismatched_info[0]:
        print (mismatched_info[1])
    else:  # sucess
        print (mismatched_info[1])