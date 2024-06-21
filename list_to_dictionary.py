lst1 = [1, 2, 3, 4]
lst2 = [2, 3, 4, 5]

dc = {}
ind = 0
for i in lst1:
    dc[i] = lst2[ind]
    ind += 1

print(f"==>> dc: {dc}")

# other method
print(f"==>> dc: {dict(zip(lst1, lst2))}")


# Now check for tupple pairs
print(f"==>> dc: {tuple(zip(lst1, lst2))}")
