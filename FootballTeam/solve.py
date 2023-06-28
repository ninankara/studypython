import heapq

#heappush : push item into heap
#heappop : pop the smallest item
#heapreplace : pop and replace
#heapify : sort

def make_team(players) :
    '''
    players : 학생들의 정보가 들어있는 리스트.
    
    players 값 예시
    [
        [학생1 이름, 학생1 슈팅, 학생1 드리블],
        [학생2 이름, 학생2 슈팅, 학생2 드리블],
        [학생3 이름, 학생3 슈팅, 학생3 드리블],
        ...
    ]
    '''
    aliceTeam = []
    chaserTeam = []

    shootrost = []
    dribblerost = []

    topshoots = []
    topdribbles = []

    for player in players:

        heapq.heappush(shootrost, (-player[1], player[0]))
    
    for player in players:
        heapq.heappush(dribblerost, (-player[2], player[0]))
    
    print(shootrost)
    print(dribblerost)

    # sorting process
    teamCnt = len(players) // 2
    print(teamCnt)

    # for i in range(len(players)):
    #     topshoot = heapq.heappop(shootrost)
    #     topshoots.append(topshoot)
    #     topdribble = heapq.heappop(dribblerost)
    #     topdribbles.append(topdribble)
    
    # print(topshoots)
    # print(topdribbles)

    while len(aliceTeam) < teamCnt:
        player = heapq.heappop(shootrost)
        print(player)
        if player[1] not in chaserTeam:  
            aliceTeam.append(player[1])
        else:
            continue
        if len(chaserTeam) < teamCnt:
            player = heapq.heappop(dribblerost)
            if player[1] not in aliceTeam:
                chaserTeam.append(player[1])
    
    while len(chaserTeam) < teamCnt:
        print(chaserTeam)
        player = heapq.heappop(dribblerost)
        if player[1] not in aliceTeam:
            chaserTeam.append(player[1])
    
    # 반환값은 두 개의 리스트가 들어있는 튜플이어야 합니다.
    # 첫 번째 리스트는 엘리스 팀, 두 번째 리스트는 체셔 팀의 선수 명단입니다.
    return (aliceTeam, chaserTeam)

# 권도안 이숙호 김미희 A
# 소윤주 김덕배 배예린 B


