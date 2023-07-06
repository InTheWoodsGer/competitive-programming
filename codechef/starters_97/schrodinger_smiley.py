"""
Sample
Input
4
3
:(:
8
(::))):(
10
:)):):(():
2
)(
Output
0
1
2
0
"""

for tc in range(int(input())):
    n = int(input())
    s = input()

    if s.find(":") == -1:
        print(0)
        continue

    s = s[s.find(":") + 1:s.rfind(":")].split(":")
    cnt = 0
    for i in s:
        if len(i) > 0 and i.count("(") == 0:
            cnt += 1
    print(cnt)
