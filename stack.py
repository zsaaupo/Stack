"""Stack"""
print(__doc__)


# stack_01 = []


# def push(stack, value):
#     stack.append(value)


# def pop(stack):
#     if len(stack) == 0:
#         print("stack is Empty")
#     else:
#         stack.pop()
    

# def peek(stack):
#     if len(stack) == 0:
#         return "stack is empty"
#     return stack[len(stack_01) - 1]


# def empty(stack):
#     if len(stack) == 0:
#         return True
#     else:
#         return False


# push(stack_01, 1)
# push(stack_01, 2)
# push(stack_01, 3)
# push(stack_01, 4)
# push(stack_01, 5)
# push(stack_01, 6)


# print("after push", "\n", stack_01)


# pop(stack_01)
# pop(stack_01)
# pop(stack_01)


# print("After pop", "\n", stack_01)


# print(peek(stack_01))


# print(empty(stack_01))


class Stack():


    def __init__(self, stack):
        self.stack = stack

    
    def push(self, value):
        self.stack.append(value)
        return self.stack


    def pop(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            self.stack.pop()


    def peek(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            return self.stack[len(self.stack) - 1]
    
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False




obj_01 = Stack([])


obj_01.push(6)
obj_01.push(5)
obj_01.push(4)
obj_01.push(3)
obj_01.push(2)
obj_01.push(1)


print("after push", obj_01.stack)


obj_01.pop()
obj_01.pop()
obj_01.pop()


print("after pop", obj_01.stack)


print(obj_01.peek())


print(obj_01.is_empty())