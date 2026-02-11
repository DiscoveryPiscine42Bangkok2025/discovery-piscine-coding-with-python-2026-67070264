old =  [2, 8, 9, 48, 8, 22, -12, 2]
new = []
new2 = []
print(f"Old Array: {old}")

for i in old:
    new.append(i + 2)

for i in new:
    if i > 5:
        new2.append(i)

print(set(new2))