from order import processOrder
from order import orderInfo

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    p = int(input())

    orders = []

    for i in range(p) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))

if __name__ == "__main__":
    main()


