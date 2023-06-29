"""
Sample
Input
3
3 10 1
4 7 10
3 10 2
4 7 10
4 10 5
1 2 3 4
Output
Yes
No
Yes
"""

"""
    n - number of weeds
    m - total number of days
    k - number of sprays to kill a weed
    a - list of days on which new weeds show up
"""
for tc in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    if a[-1] + k - 1 <= m:
        print("yes")
    else:
        print("no")
