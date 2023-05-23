

e, s, m = map(int, input().split())

if e == 15:
    e = 0
if s == 28:
    s = 0
if m == 19:
    m = 0

ans = 0

for x in range(1, 7981):
    if x % 15 == e and x % 28 == s and x % 19 == m:
        ans = x
        break

if ans == 0:
    ans = 7980

print(ans)
