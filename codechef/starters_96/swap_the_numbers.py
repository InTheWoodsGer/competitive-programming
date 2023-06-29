"""
Sample
Input
2
3 2
3 2 1
4 3
3 2 4 1
Output
1 2 3
1 2 4 3
"""

"""
    n - array length
    k - distant between elements while swapping
    a - elements
"""
for tc in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n <= k:
        # no elements can be swapped
        print(" ".join(map(str, a)))
    elif k <= n//2:
        # all elements can be swapped, so every permutation of the elements can be achieved
        print(" ".join(map(str, sorted(a))))
    else:
        # in the middle there are some elements which can't be swapped
        # elements at the beginning and the end of the array can be sorted in every possible way
        movable_elements = sorted(a[:n-k] + a[-(n-k):])
        print(" ".join(map(str, movable_elements[:n-k] + a[n-k:-(n-k)] + movable_elements[n-k:])))
