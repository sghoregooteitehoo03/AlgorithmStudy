# A = 10, Z = 35
N, B = input().split()
str_len = len(N)

answer = 0
for i in range(str_len):
    c = N[i]
    if c.isdigit():
        answer += int(c) * (int(B) ** (str_len - i - 1))
    else:
        answer += (ord(c) - 55) * (int(B) ** (str_len - i - 1))

print(answer)