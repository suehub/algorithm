import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().rstrip()

for x in croatia:
    s = s.replace(x, '*')

print(len(s))