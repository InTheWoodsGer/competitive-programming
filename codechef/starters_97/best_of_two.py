"""
Sample
Input
3
3 2 5 6 1 1
4 4 5 6 4 1
6 6 6 6 6 1
Output
Alice
Bob
Tie
"""

for tc in range(int(input())):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    a = a1 + a2 + a3 - min(a1, a2, a3)
    b = b1 + b2 + b3 - min(b1, b2, b3)

    if a > b:
        print("Alice")
    elif a == b:
        print("Tie")
    else:
        print("Bob")
