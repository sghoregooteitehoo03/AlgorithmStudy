# https://www.acmicpc.net/problem/10825
n = int(input())
student = []

for i in range(n):
    name, kor, eng, math = input().split()
    grades = [int(kor), int(eng), int(math)]

    student.append((name, grades))

student.sort(key = lambda x: (-x[1][0], x[1][1],-x[1][2], x[0]))
for s in student:
    print(s[0])