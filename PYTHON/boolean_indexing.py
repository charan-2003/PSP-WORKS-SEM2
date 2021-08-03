import numpy as np
names = np.array(["Bob","Joe","Will","Bob","Will","Joe","Joe"])
data = np.random.randn(7,4)
print(names)
print(data)

print(names == "Bob")
print(names == "Bob")

print(data[names == "Bob",3])
print(names!= "Bob")
cond = names == "Bob"
print(data[~cond])

mask = (names == "Bob") | (names == "Will")
print(mask)
print(data[mask])

print(data[names!= "Joe"])
print(data)