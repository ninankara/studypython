class LinkedListElement :
    def __init__(self, val, p, n) :
        self.value = val
        self.myPrev = p



        self.myNext = n
        
class Deque:
    '''
    아래의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        문제의 조건대로 값들을 담을 수 있게끔 
        Deque 클래스의 생성자를 자유롭게 정의하세요.
        '''
        self.start = None
        self.end = None
        self.count = 0




    def push_front(self, n) :
        '''
        덱에 정수 n을 맨 앞에 넣습니다.
        '''
        if self.start == None and self.end == None :
            elem = LinkedListElement(n, None, None)
            self.start = elem
            self.end = elem
        else :
            elem = LinkedListElement(n, None, self.start)
            self.start.myPrev = elem



            self.start = elem
        
        self.count += 1







        return
    
    def push_back(self, n) :
        '''
        덱에 정수 n을 맨 뒤에 넣습니다.
        '''
        if self.start == None and self.end == None :
            elem = LinkedListElement(n, None, None)
            self.start = elem
            self.end = elem
        else :
            elem = LinkedListElement(n, self.end, None)
            self.end.myNext = elem
            self.end = elem
        
        self.count += 1




        return

    def pop_front(self) :
        '''
        덱에서 가장 앞에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1 :



            return
        
        if self.count >= 2 :
            nextNode = self.start.myNext
            nextNode.myPrev = None
            self.start = nextNode
        else :
            self.start = None
            self.end = None
        
        self.count -= 1
        return




    def pop_back(self) :
        '''
        덱에서 가장 뒤에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1 :



            return
        
        if self.count >= 2 :
            prevNode = self.end.myPrev
            prevNode.myNext = None
            self.end = prevNode
        else :
            self.start = None
            self.end = None
        
        self.count -= 1
        return




    def size(self) :
        '''
        덱에 들어 있는 정수의 개수를 return 합니다.
        '''
        return self.count

    def empty(self) :
        '''
        덱이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size() == 0 :
            return 1
        return 0

    def front(self) :
        '''
        덱의 가장 앞에 있는 정수를 return 합니다. 만약 덱에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1 :
            return -1
        return self.start.value

    def back(self) :
        '''
        덱의 가장 뒤에 있는 정수를 return 합니다. 만약 덱에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1 :
            return -1
        return self.end.value