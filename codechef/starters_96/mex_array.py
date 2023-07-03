"""
Sample
Input
4
5
0 1 2 2 3
1
1
2
0 0
6
0 0 0 1 2 4
Output
2
4 0
1
0
2
1 1
3 1 1 0
"""

from collections import Counter

for tc in range(int(input())):
    n = int(input())
    a = Counter(list(map(int, input().split())))

    b = []
    i = 0
    complete_sequences = 0
    while i in a:
        if i == 0:
            complete_sequences = a[0]

        if complete_sequences <= a[i]:
            a[i] -= complete_sequences
        elif a[i] < complete_sequences:
            b = ([str(i)] * (complete_sequences - a[i])) + b
            complete_sequences = a[i]
            a[i] = 0

        i += 1

    if complete_sequences:
        b = ([str(i)] * complete_sequences) + b

    b += ["0"] * sum(a.values())
    print(len(b))
    print(" ".join(b))
