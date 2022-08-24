N = int(input())
arr = list(map(int, input().split()))
students = int(input())
sex = []
for i in range(students):
    sex.append(list(map(int, input().split())))

for i in sex:

    if i[0] == 1:
        for j in range(len(arr)):
            if (j + 1) % i[1] == 0:
                arr[j] = int(not arr[j])
    else:
        for j in range(len(arr)):
            if (j + 1) == i[1]:
                plus = j + 1
                minus = j - 1
                arr[j] = int(not arr[j])
                while True:

                    if minus >= 0 and plus < len(arr):
                        if arr[minus] == arr[plus]:
                            arr[minus] = int(not arr[minus])
                            arr[plus] = int(not arr[plus])
                        else:
                            break
                    else:
                        break

                    minus -= 1
                    plus += 1

count = 0
while count < len(arr):

    print(arr[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1
