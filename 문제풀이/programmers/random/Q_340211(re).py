# 시뮬레이션 문제

from collections import deque
from collections import defaultdict

def solution(points, routes):
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

        if current_robot in arrived.keys():
            continue

        if arrived_point[0] == current_i and arrived_point[1] == current_j:
            arrived[current_robot] = robot_history
            continue

        if (current_i + 1) < 101 and current_robot not in history[((current_i + 1), current_j)]:
            new_history = robot_history + [(current_i + 1, current_j, time + 1)]
            queue.append(
                (
                    current_i + 1,
                    current_j,
                    current_robot,
                    arrived_point,
                    time + 1,
                    new_history,
                )
            )
            history[((current_i + 1), current_j)].append(current_robot)

        if (current_i - 1) >= 0 and current_robot not in history[((current_i - 1), current_j)] == []:
            new_history = robot_history + [(current_i - 1, current_j, time + 1)]
            queue.append(
                (
                    current_i - 1,
                    current_j,
                    current_robot,
                    arrived_point,
                    time + 1,
                    new_history,
                )
            )
            history[((current_i - 1), current_j)].append(current_robot)

        if (current_j + 1) < 101 and current_robot not in history[(current_i, current_j + 1)]:
            new_history = robot_history + [(current_i, current_j + 1, time + 1)]
            queue.append(
                (
                    current_i,
                    current_j + 1,
                    current_robot,
                    arrived_point,
                    time + 1,
                    new_history,
                )
            )
            history[(current_i, current_j + 1)].append(current_robot)

        if (current_j - 1) >= 0 and current_robot not in history[(current_i, current_j - 1)]:
            new_history = robot_history + [(current_i, current_j - 1, time + 1)]
            queue.append(
                (
                    current_i,
                    current_j - 1,
                    current_robot,
                    arrived_point,
                    time + 1,
                    new_history,
                )
            )
            history[(current_i, current_j - 1)].append(current_robot)

    answer = 0
    for i in range(1, len(routes)):
        current_robot_routes = set(arrived[i])

        for j in range(i + 1, len(routes) + 1):
            other_robot_routes = set(arrived[j])

            answer += len(current_robot_routes & other_robot_routes)

    return answer


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
