from collections import defaultdict

def solution(tickets):
    global max_result
    max_result = 'Z'
    tickets_graph = defaultdict(list)
    make_graph(tickets, tickets_graph)
    for i in tickets_graph['ICN']:
        # 초기 노드 및 초기값 설정
        i[1] = 1
        find_path(tickets_graph, i, 'ICN,' + i[0], 1, len(tickets))
        i[1] = 0
    return max_result.split(',')

# 그래프 방식으로 해결
def make_graph(tickets, tickets_graph):
    for ticket in tickets:
        # ticket = [departure, arrival]
        # 딕셔너리 key -> deaprture value -> [arrival, checked] checked는 0: 미방문, 1: 방문
        tickets_graph[ticket[0]].append([ticket[1], 0])

def find_path(tickets_graph, next_airport, result, cnt, end_cnt):
    # 재귀방식의 dfs
    global max_result
    if cnt == end_cnt:
        # 문자열 비교해서 ABC 순으로 서열 체크
        if max_result > result:
            max_result = result
        return

    for i in tickets_graph[next_airport[0]]:
        if i[1] == 0:
            # 방문 노드 체크
            i[1] = 1
            find_path(tickets_graph, i, result + ',' + i[0], cnt+1, end_cnt)
            # 종료된 재귀는 방문 노드 초기화
            i[1] = 0
    
    return

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])