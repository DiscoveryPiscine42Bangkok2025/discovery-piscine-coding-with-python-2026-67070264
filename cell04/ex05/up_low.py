txt = input()
ans = ""
for i in txt:
    if i == i.upper():
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)