def trans(data):
    return data[1]


n = int(input())
students = []

for i in range(n):
    name, grade = input().split()
    students.append((name, int(grade)))

result = sorted(students, key = trans)
for s in result:
    print(s[0], end=' ')