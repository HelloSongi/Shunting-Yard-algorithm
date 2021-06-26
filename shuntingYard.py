
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
    
    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)           

    def pop(self):
        result = -1

        if self.stack != []:
            result = self.stack.pop()

        return result
    
    def display(self):
        if self.stack == []:
            print("Stack is empty!")
        else:
            print("Stack data:")
            for item in reversed(self.stack):
                print(item)
    
    def isEmpty(self):
        return self.stack == []
    
    def topChar(self):
        result = -1

        if self.stack != []:
            result = self.stack[len(self.stack) - 1]

        return result


def isNumber(c):
    return c >= '0' 

operators = "+-*/^"

def isOperator(c):
    return c in operators

def getPrecedence(c):
    result = 0

    for char in operators:
        result += 1

        if char == c:
            if c in '-/':
                result -= 1
            break

    return result

def operator_usage(a, b, operators):
     
        if operators == '+': 
             return a + b
        elif operators == '-': 
            return a - b
        elif operators == '*': 
            return a * b
        elif operators == '/': 
            return a / b
        elif operators == '^': 
            return a ** b


def shuntigYard(expression):
    result = ""

    stack = Stack(15)

    for char in expression:
        if isNumber(char):
            result += char
        elif isOperator(char):
            while True:
                topChar = stack.topChar()

                if stack.isEmpty() or topChar == '(':
                    stack.push(char)
                    break
                else:
                    pC = getPrecedence(char)
                    pTC = getPrecedence(topChar)

                    if pC > pTC:
                        stack.push(char)
                        break
                    else:
                        result += stack.pop()

        elif char == '(':
            stack.push(char)
        elif char == ')':
            cpop = stack.pop()

            while cpop != '(':
                result += cpop
                cpop = stack.pop()
                #result.append(operator_usage(cpop, char, operators))   .....evaluate if a closing parethesis is encountered
    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop
        #result.append(operator_usage(cpop, char, operators))   ......... evalute the postfix if stack is empty
    return result
    #return result[-1]   ....... top of the result have the answer


#main function
if __name__ == "__main__":                                
    while True:
        choice = input('1. Enter an expression   or     2. Assign a variable:  ')
        if choice == '1':
            expression = input('enter your expression: ')
            print(shuntigYard(expression))
            
        elif choice == '2':
            print('finish this section soon')
        elif choice == '!':
            break
    print("You've program terminated")
