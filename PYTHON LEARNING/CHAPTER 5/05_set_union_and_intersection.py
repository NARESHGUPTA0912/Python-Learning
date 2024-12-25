s1 = {1, 45, 47}
s2 = {7,45, 6, 44}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1-s2)
print(s2-s1)

print({6,7}.issubset(s2))