###
input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
output
13
####





set0 = set()
n = int(input())
nl = set ( input().split())
b = int (input())
nr = set (input().split())
print(len(nl | nr))



