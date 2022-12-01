# cook your dish here
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    pieces = [i for i in range(1, n + 1)]
    index, summ = 0, 0
    if n == 1:
        print(0)
    else:
        while k > index:
            if pieces[index] < pieces[len(pieces) - index - 1]:
                pieces[index], pieces[len(pieces) - index - 1] = pieces[len(pieces) - index - 1], pieces[index]
            index += 1
            if index >= k:
                break
        index = 0
        for j in range(0, n - 1):
            num = pieces[index]
            for i in range(index + 1, n):
                if num > pieces[i]:
                    summ += 1
            index += 1
        print(summ)

