# 키-값 형식에 키에는 시작지점을 값 부분에는 갈 수 있는 곳을 리스트로 담음
# 값을 오름차순으로 정렬
# 큐에 인천을 넣고 그 갈수있는 지점을 큐에 담음
# DFS로 타고 들어가 방문 지점을 정답에 담아 반환
from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)

    for start, end in tickets:
        routes[start].append(end)

    for values in routes.values():
        values.sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    return path[::-1]

print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))