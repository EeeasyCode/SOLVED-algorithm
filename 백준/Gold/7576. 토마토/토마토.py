from collections import deque


def solution(m, n, tomatoes):
    count = 0  # Count number of days
    deq = deque()
    # deq = list()
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def search(row, col):
        searched_list = []

        for i, j in D:
            if (row + i < N and col + j < M) and (row + i >= 0 and col + j >= 0):
                if tomatoes[row + i][col + j] == 0:
                    tomatoes[row + i][col + j] = 1
                    searched_list.append((row + i, col + j))

        return searched_list

    # Add all riped tomatoes
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 1:
                deq.append((r, c))

    # Search begin
    while deq:
        for _ in range(len(deq)):
            r, c = deq.popleft()
            for tomato in search(r, c):
                deq.append(tomato)
        count += 1

    # Check unriped tomato(es) after search
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 0:
                return -1

    return count - 1


if __name__ == "__main__":
    M, N = map(int, input().split(" "))
    tomatoes = [[int(n) for n in input().split(" ")] for _ in range(N)]
    print(solution(M, N, tomatoes))
