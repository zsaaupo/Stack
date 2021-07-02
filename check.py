"""Checking"""
print(__doc__)


# p = "(()"


# stack_01 = []

# for i in range(len(p)):
#     if p[i] == "(":
#         stack_01.append("(")
#     elif p[i] == ")":
#         stack_01.pop()

# print(stack_01)

class Check():

    def __init__(self, parenthesis):
        self.parenthesis = parenthesis

    def check(self):
        
        stack = []

        for i in range(len(self.parenthesis)):

            if self.parenthesis[i] == "(":
                stack.append("(")

            elif self.parenthesis[i] == ")":
                stack.pop()

        if len(stack) == 0:
            return "parentheses balanced"
        else:
            return "parentheses not balanced"


obj_01 = Check("(()")

print(obj_01.check())
