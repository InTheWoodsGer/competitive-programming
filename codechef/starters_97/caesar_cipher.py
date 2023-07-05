"""
Sample
Input
3
3
abc
bcd
cde
2
bd
zb
dd
4
code
xjyz
chef
Output
def
bb
xcza
"""

for tc in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    u = input()

    k = ord(t[0]) - ord(s[0])
    if k < 0:
        k += 26

    shifted_u = ''
    for original_char in u:
        shifted_u += chr(ord(original_char) + k - (26 if ord(original_char) + k > 122 else 0))
    print(shifted_u)
