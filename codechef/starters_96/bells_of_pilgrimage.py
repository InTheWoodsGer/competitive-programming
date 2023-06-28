"""
Sample
Input
4
6 2 0 80
6 2 1 80
6 2 4 80
6 2 6 80
Output
80
90
110
140
"""

"""
    n - number of bells to ring
    x - number of bells which increase mana by 10
    k - bells rung so far
    p - initial mana
"""
for tc in range(int(input())):
    n, x, k, p = map(int, input().split())

    p += min(x, k) * 10
    p += max(k - x, 0) * 5
    p += 20 if k == n else 0

    print(p)