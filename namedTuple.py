from collections import namedtuple

nmbr = int(input())
columns = input().split()
total = 0
for _ in range(nmbr):
    students = namedtuple('students',columns)
    stud = students(*input().split())
    total += int(stud.MARKS)

avg = total/nmbr
print(round(avg,2))
