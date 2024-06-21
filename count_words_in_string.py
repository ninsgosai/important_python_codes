
sentense = input("Enter your string.")
diko = {}
# for i in sentense.lower().split(" "):
#     if i not in diko:
#         diko[i] = 0
#     diko[i] = diko[i] + 1

# other short method
for i in sentense.lower().split(" "):
    diko[i] = diko.get(i, 0) + 1

print(f"==>> diko: {diko}")
