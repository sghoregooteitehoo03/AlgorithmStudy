# 시뮬레이션 문제
# 각 보드판 위에 같은 시간대에 겹치는 로봇이 생기면 카운트
# 최적의 경로를 기록
# set을 통해 겹치는게 몇개인지 확인

from collections import deque
from collections import defaultdict


def solution(points, routes):
    answer = 0
    board = [["X"] * 101 for _ in range(101)]

    for point in points:
        board[point[0]][point[1]] = "O"

    history = defaultdict(list)
    queue = deque([])
    for i in range(len(routes)):
        route = routes[i]
        point = points[route[0] - 1]
        arrived_point = points[route[1] - 1]

        queue.append((point[0], point[1], i + 1, arrived_point, 0, []))
        history[(route[0], route[1])].append(i + 1)

    arrived = defaultdict(list)
    while queue:
        current_i, current_j, current_robot, arrived_point, time, robot_history = (
            deque.popleft(queue)
        )

        if arrived_point[0] == current_i and arrived_point[1] == current_j:
            arrived[current_robot].append(robot_history)

        if (current_i + 1) < 101 and history[((current_i + 1), current_j)] == []:
            queue.append(
                current_i + 1,
                current_j,
                current_robot,
                arrived_point,
                time + 1,
                robot_history + [(current_i + 1, current_j, time + 1)]
            )
        if (current_i - 1) >= 0 and history[((current_i - 1), current_j)] == []:
            queue.append(
                current_i - 1,
                current_j,
                current_robot,
                arrived_point,
                time + 1,
                robot_history + [(current_i - 1, current_j, time + 1)]
            )
        if (current_j + 1) < 101 and history[(current_i, current_j + 1)] == []:
            queue.append(
                current_i,
                current_j + 1,
                current_robot,
                arrived_point,
                time + 1,
                robot_history + [(current_i, current_j + 1, time + 1)]
            )
        if (current_j - 1) >= 0 and history[(current_i, current_j - 1)] == []:
            queue.append(
                current_i,
                current_j - 1,
                current_robot,
                arrived_point,
                time + 1,
                robot_history + [(current_i, current_j - 1, time + 1)]
            )

    print(arrived)
    return answer


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
