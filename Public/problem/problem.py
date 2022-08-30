import heapq

# 시작점 찾기
def find(x, pre_subject):
    if x not in pre_subject.keys(): # 선수 과목이 없는 경우
        first_node.add(x)
    else:
        for ele in pre_subject[x]:
            if ele not in first_node:
                find(ele, pre_subject)

def solution(s1, s2, k):  
    answer = []

    # 선수과목 정보 업데이트
    pre_subject = {} # 선수과목: 들을 수 있는 과목
    for i in range(len(s1)):
        pre_subject[s2[i]] = pre_subject.get(s2[i], []) + [s1[i]]
    
    # 시작 가능한 노드 찾기
    global first_node
    first_node = set()
    find(k, pre_subject)

    # 이수해야 하는 과목 순서 찾기
    data = []
    for ele in first_node:
        heapq.heappush(data, [1, ele])

    # 후수과목 업데이트
    next_subject = {}
    for i in range(len(s1)):
        next_subject[s1[i]] = next_subject.get(s1[i], []) + [s2[i]]
    
    while data:
        ele = heapq.heappop(data)
        
        # 선수 과목이 모두 있는지 확인
        if ele[1] not in pre_subject.keys() or set(answer)&set(pre_subject[ele[1]]) == set(pre_subject[ele[1]]):
            answer.append(ele[1])
        else:
            heapq.heappush(data, [ele[0]+1, ele[1]])
            continue
        
        if ele[1] == k: # 원하는 과목까지 도달했을 경우 
            break

        # 후수 과목 찾기
        if ele[1] not in next_subject.keys(): # 후수 과목이 없는 경우
            continue
        
        for s in next_subject[ele[1]]:
            if [2, s] not in data:
                    heapq.heappush(data, [2, s])

    return answer


print(solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"], ["G", "C", "G", "F", "J", "E", "B", "F", "B"], "G"))