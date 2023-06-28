"""
Sample 1
Input
4 7
Output
17

Sample 2
Input
1 6
Output
1
"""

a, b = map(int, input().split())
print(abs(a*b - (a+b)))

