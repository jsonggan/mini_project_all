

def merge(array, p, q, r, byfunc=None):
    nleft = q - p +1
    nright = r - q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left = 0
    right = 0
    dest = p
    
    while left<nleft and right<nright:
        compare_leq = None
        if byfunc == None:
            compare_leq = left_array[left]<=right_array[right]
        else:
            compare_leq = byfunc(left_array[left])<=byfunc(right_array[right])

        if compare_leq:
            array[dest] = left_array[left]
            left += 1
            dest += 1
        
        else:
            array[dest] = right_array[right]
            right += 1
            dest += 1
    
    while left<nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right<nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r, byfunc=None):
    if r -p >0:
        q = int((p+r)/2)
        mergesort_recursive(array,p,q,byfunc)
        mergesort_recursive(array,q+1,r,byfunc)
        merge(array,p,q,r,byfunc)
        

def mergesort(array, byfunc=None):
    mergesort_recursive(array,0,len(array)-1,byfunc)

class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        n = len(self.__items)
        if self.size > 0:
            popped_item = self.__items.pop(self.size-1)
            return popped_item
        else:
            return None
    
    def peek(self):
        n = len(self.__items)
        return self.__items[n-1]

    @property
    def is_empty(self):
        if self.__items == []:
            return True
        else:
            return False

    @property
    def size(self):
        n = len(self.__items)
        return n

class EvaluateExpression:

    valid_char = '0123456789+-*/() '
    
    def __init__(self, string=""):
        self.expression = string

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, new_expr):
        bool1 = True

        if not isinstance(new_expr,str):
            bool1 = False

        for i in new_expr:
            if i not in EvaluateExpression.valid_char:
                bool1 = False

        if bool1 == True:
            self._expression = new_expr
        else:
            self._expression = ""
    def insert_space(self):
        spaced = ""
        for i in self.expression:
            if i in "()/+-*":
                spaced = spaced + " " + i + " "
            else:
                spaced += i
        return spaced
	
    def process_operator(self, operand_stack, operator_stack):
        number1 = str(operand_stack.pop())
        number2 = str(operand_stack.pop())
        operator = str(operator_stack.pop())
        operand_stack.push(int(eval(number2+operator+number1)))
    
    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        for index,i in enumerate(tokens):
            if i in "1234567890":
                operand_stack.push(i)
            if i in "+-":
                while (operator_stack.size != 0 ) and (operator_stack.peek() not in "()"):
                    self.process_operator(operand_stack,operator_stack)
                operator_stack.push(i)
            if i in "*/":
                while operator_stack.size !=0 and operator_stack.peek() in '*/':
                    self.process_operator(operand_stack,operator_stack)
                operator_stack.push(i)
            if i== '(':
                operator_stack.push(i)
            if i == ')':
                while operator_stack.peek() != '(':
                    self.process_operator(operand_stack,operator_stack)
                operator_stack.pop()
            if index+1 == len(tokens):
                self.process_operator(operand_stack,operator_stack)
        return operand_stack.pop()
            

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





