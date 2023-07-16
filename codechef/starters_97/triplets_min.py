"""
Sample
Input
2
6 2
3 3 3 3 3 3
18
1
4 4
2 4 2 1
1
2
3
4
Output
3
3
1
1
1
2
"""
import bisect

for tc in range(int(input())):
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))[:-2]

    occurrences = list()
    occurrences_sum = 0
    for i in range(n - 2):
        occurrences_sum += ((n - (i + 1)) * (n - (i + 2))) // 2
        occurrences.append(occurrences_sum)

    for i in range(q):
        print(a[bisect.bisect_left(occurrences, int(input()))])
