'''
Queue 클래스를 구현하세요.
'''
class Node :
    def __init__(self, value) :
        self.value = value
        self.next = None

class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, n) :
        '''
        queue에 정수 n을 넣습니다.
        '''
 
        new_node = Node(n)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.is_empty():
            return
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return self.size

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size == 0 :
            return 1
        else :
            return 0

    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.is_empty():
            return -1
        return self.head.value

    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.is_empty():
            return -1
        return self.tail.value
'''
Queue 클래스를 구현하세요.
'''

# class Queue:
#     '''
#     List를 이용하여 다음의 method들을 작성하세요.
#     '''
#     def __init__(self) :
#         '''
#         큐 myQueue을 만듭니다.
#         '''
#         self.myQueue = []

#     def push(self, n) :
#         '''
#         queue에 정수 n을 넣습니다.
#         '''
#         self.myQueue.append(n)

#     def pop(self) :
#         '''
#         queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
#         '''
#         if self.empty() == 1:
#             return
#         del self.myQueue[0]

#     def size(self) :
#         '''
#         queue에 들어 있는 정수의 개수를 return 합니다.
#         '''
#         return len(self.myQueue)

#     def empty(self) :
#         '''
#         queue이 비어있다면 1, 아니면 0을 return 합니다.
#         '''
#         if self.size() == 0 :
#             return 1
#         else :
#             return 0

#     def front(self) :
#         '''
#         queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
#         '''
#         if self.empty()==1:
#             return -1
#         return self.myQueue[0]

#     def back(self) :
#         '''
#         queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
#         '''
#         if self.empty() == 1:
#             return -1
#         return self.myQueue[-1]
        
        