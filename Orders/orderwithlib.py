from queue import Queue  

class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v
        
def selectQueue(normalQueue, vipQueue, time, orders):
    normalIndex = -1 if len(normalQueue.queue) == 0 else normalQueue.queue[0]
    vipIndex = -1 if len(vipQueue.queue) == 0 else vipQueue.queue[0]

    if vipIndex == -1 :
        return normalQueue

    if normalIndex == -1:
        return vipQueue
    
    if time < orders[normalIndex].time and time < orders[vipIndex].time :

        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue
            
        if time >= orders[normalIndex].time and time < orders[vipIndex].time:
            return normalQueue
            
        if time >= orders[vipIndex].time and time < orders[normalIndex].time:
            return vipQueue

        return vipQueue
    return vipQueue

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''

    result = []
    
    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1

    for i in range(len(orders)) :
        curTime = orders[i].time 

        if orders[i].vip == 0:
            normalQueue.put(i)
        else:
            vipQueue.put(i)
        
        while jobEndTime <= curTime and not(normalQueue.empty() and vipQueue.empty()):
           targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime,orders) 
           index = targetQueue.queue[0]

           jobEndTime = max(jobEndTime,orders[index].time) + orders[index].duration
           result.append(index+1)
           targetQueue.get()

    while not(normalQueue.empty() and vipQueue.empty()):
        targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime,orders) 
        index = targetQueue.queue[0]

        jobEndTime = max(jobEndTime,orders[index].time) + orders[index].duration
        result.append(index+1)
        targetQueue.get()


    return result