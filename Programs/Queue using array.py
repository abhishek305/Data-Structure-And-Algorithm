


class Queue:
    def __init__(self):
        self.array=[]
    def enqueue(self,items):
        return self.array.append(items)    
    def dequeue(self):
        return self.array.pop(0) 
    def head(self):
        return self.array[0]
    def tail(self):
        return self.array[-1]
    def isEmpty(self):
        if len(self.array)==0:
            raise Exception("Queue Empty")
        return self.array    
            
new =Queue()

new.enqueue('5')
new.enqueue('6')
new.enqueue('7')
new.enqueue('8')
new.enqueue('22')
pop = new.tail()
print(pop)
print(new.isEmpty())



