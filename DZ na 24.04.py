strs = list(input().split())
strs.sort(key=len, reverse=True)
a = strs.pop()
ans = ''
for i in range(len(a)):
    flag = 1
    for st in strs:
        if st[i] != a[i]:
            flag = 0
    if flag:
        ans+=a[i]
    else:
        break
print(ans)