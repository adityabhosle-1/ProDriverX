class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, data):
        ''' Pushes a element to top of the stack '''
        if(self.isFull() != True):
            self.index.append(data)
        else:
            print('Stack overflow')

    def pop(self):
        ''' Pops the top element '''
        if(self.isEmpty() != True):
            return self.index.pop()
        else:
            print('Stack is already empty!')

    def isEmpty(self):
        ''' Checks whether the stack is empty '''
        return len(self.index) == []

    def isFull(self):
        ''' Checks whether the stack if full '''
        return len(self.index) == self.size

    def peek(self):
        ''' Returns the top element of the stack '''
        if(self.isEmpty() != True):
            return self.index[-1]
        else:
            print('Stack is already empty!')

    def stackSize(self):
        ''' Returns the current stack size '''
        return len(self.index)
    
    def __str__(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

    

if __name__ == '__main__':
    print("**Creating the Stack**")
    Size = int(input("Define the size of Stack: "))
    myStack = Stack(Size)
    while True:

        print("\n**Operations**")
        print("1. Push the element")
        print("2. Peek element")
        print("3. Pop the element")
        print("4. Is stack Empty?")
        print("5. Display")
        print("6. Exit")
        
        menu = int(input("\nChoose an action: "))
        
        if menu == 1:
            value = int(input("Enter the required value: ")) 
            myStack.push(value)
        elif menu == 2:
            if len(myStack.index)==0:
                print("The Stack is Empty\n")            
            else:
                print("The top element of the stack is %d\n" % myStack.peek())
        elif menu == 3:
            if len(myStack.index)==0:
                print("The Stack is Empty\n")
            else:
                print("The element popped out of the stack is %d\n"%myStack.pop())
        elif menu == 4:
            con = False
            if len(myStack.index)==0:
                con = True
            print("Emptyness of the stack is %r\n"%con)
        elif menu == 5:
            if len(myStack.index)==0:
                print("The Stack is Empty\n")
            else:
                print("The elemnts in the stack are:",myStack)
                print('\n')
        elif menu == 6:
            break
        else:
            print("You have entered Wrong Choice\n")