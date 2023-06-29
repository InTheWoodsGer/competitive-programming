"""
Sample
Input
3
5 3
1 3 5
4 2
1 3
3 1
2
Output
6
6
4
"""

"""
    n - length of the original set
    m - number of elements in the expected set
    q - elements in the expected set
"""

for tc in range(int(input())):
    n, m = map(int, input().split())
    q = set(map(int, input().split()))

    print(((n * (n + 1)) // 2) - sum(q))
