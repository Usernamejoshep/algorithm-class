#define Stack class with push, pop, is_empty
class ArraysTack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity -1

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item 
            print(f"PUSH: {item!r} -> stack is now {self.array[:self.top + 1]}")       
        else:
            raise OverflowError("stack Overflow")  #pass
        
    def pop(self): 
        if not self.is_empty():
            

            item = self.array[self.top] 
            self.array[self.top] = None
            self.top -= 1  
            print(f"pop : {item!r} -> stack is now {self.array[:self.top +1]}")
            return item
        else:
             raise IndentationError("stack underFlow")

    def peek(self):
        if not self.is_empty():
          return self.array[self.top]
        return None
    
    def size(self):
        return self.top + 1
    
def reverse_string(statement):
    print("\n[1] PUSH  1단계 -------------------------------------------------")
    stack = ArraysTack(len(statement))
    for char in statement: 
        stack.push(char)

    print("\n[2] PUSH  2단계 -------------------------------------------------")
    out = []
    while not stack.is_empty():
        out.append(stack.pop())

    result = ''.join(out)
    print(f"\n[3] 최종결과 : {result}")
    return result


if __name__ == "__main__":
    statement = "Hello,World!"
    reverse_string(statement)



    


                           