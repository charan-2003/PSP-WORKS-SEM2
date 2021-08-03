a = [1,3,5,7,9,11,13]
cummpro = []
n = len(a)
i = 1
v = a[0]
for i in a:
    v = v*i
    cummpro.append(v)

print(cummpro)
