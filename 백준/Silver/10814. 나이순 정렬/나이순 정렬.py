import sys
input = sys.stdin.readline

N = int(input())

people_arr = []

for i in range(N):
    age, name = input().split()
    people_arr.append([int(age), name, i])

people_arr = sorted(people_arr, key= lambda x: (x[0], x[2]))

for person in people_arr:
    print(f"{person[0]} {person[1]}")

