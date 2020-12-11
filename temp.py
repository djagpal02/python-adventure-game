from Map import all_maps
tags = []

for m in all_maps:
    size = len(m.matrix)
    for i in range(size):
        for j in range(size):
            if m.matrix[i][j][1] not in tags:
                tags.append(m.matrix[i][j][1])

for i in tags:
    print(i)
print(tags)