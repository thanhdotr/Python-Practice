# a =  int(input("What is the 1st number ?"))
# b = float(input("What is the 2nd number ? "))
"""Constellations"""

dic = {}
stars = [[0, 1], [16, 3], [1, 0], [2, 7], [9, 0], [4, 1], [2, 2], [8, 1], [9, 3], [15, 5]]
#
dist_list = []

constellations = []

for i in range(len(stars)):

    if i == len(stars) - 1:
        break

    else:
        reset_point = True
        shortest_dist = []

        for d in range(len(stars)):
            if i == d:
                continue
            else:
                dist = ((stars[d][0] - stars[i][0])**2 + (stars[d][1] - stars[i][1])**2)**0.5

                if reset_point:
                    shortest_dist = [i, d, dist]
                    reset_point = False

                else:
                    if shortest_dist[2] > dist:
                        shortest_dist = [i, d, dist]

                    elif shortest_dist[2] == dist:
                        shortest_dist.append([i, d, dist])


        dist_list.append(shortest_dist)
for stars in range(len(dist_list)):
    dist_list[stars] = dist_list[stars][:2]
print(dist_list)
def merge_lists(orig):
    def step(orig):
        mid = []
        mid.append(orig[0])
        for i in range(len(mid)):
            for j in range(1,len(orig)):
                for k in orig[j]:
                    if k in mid[i]:
                        mid[i].extend(orig[j])
                        break
                        print(mid)
                    elif k == orig[j][-1] and orig[j] not in mid:
                        mid.append(orig[j])
                        print(mid)
        mid = [sorted(list(set(x))) for x in mid]
        return mid

    result = step(orig)
    while result != step(result):
        result = step(result)

    return result

print(merge_lists(dist_list))

