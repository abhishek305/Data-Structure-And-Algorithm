class myStack():
    def __init__(self):
        self.stack=[]       #Empty Stack
   
    def push(self,items):
        return self.stack.append(items)  #pushing elements into stack
   
    def pop(self):
        return self.stack.pop() #poping element from one end from stack
   
        
    def stacktop(self):
        if len(self.stack)==0:   # checking if stack is empty and return the top of stack
            return "Stack Empty"
        return self.stack[-1]

    def displayStack(self):
        return self.stack  #displaying the stack

new =myStack()
new.push('2')
new.push('3')
new.push('4')
new.push('5')
new.push('6')
new.push('7')
top=new.stacktop()
print(top)
print(new.displayStack())


       