lst = [1, 2, 4, 5, 6, 7]
missing = []
for i in range(min(lst), max(lst)):
    if i not in lst:
        missing.append(i)

print(missing)


# using summetion methos
total = len(lst)
print(f"==>> sum(lst): {sum(lst)}")
print(f"==>> ((total * (total+1))/2): {((total * (total+1))/2)}")
fin_total = ((total * (total+1))/2) - sum(lst)
print(f"==>> fin_total: {fin_total}")
