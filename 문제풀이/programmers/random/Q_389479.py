# 구현으로 풀이
# 기존에 증설된 서버로 들어온 유저수를 받아들일 수 있는지를 판별해서 증설할지 말지를 결정


def solution(players, m, k):
    answer = 0
    servers = []

    for t in range(len(players)):
        player = players[t]

        i = 0
        while i < len(servers):
            servers[i] -= 1

            if servers[i] <= 0:
                servers.pop(i)
            else:
                i += 1

        if m <= player:
            if len(servers) < player // m:
                answer += (player // m) - len(servers)
                servers += [k] * ((player // m) - len(servers))

    return answer


print(
    solution(
        [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5
    )
)