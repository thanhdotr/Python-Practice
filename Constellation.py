"""Constellations"""

dic = {}
stars = [[0, 1], [16, 3], [1, 0], [2, 7], [9, 0], [4, 1], [2, 2], [8, 1], [9, 3], [15, 5]]

dist_list = []

constellations = []

for i in range(len(stars)):

    if i == len(stars) - 1:
        break

    else:
        reset_point = True
        shortest_dist = []

        for d in range(len(stars)):
            if d == i:
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

l = dist_list
taken=[False]*len(l)
l=[set(elem) for elem in l]

def dfs(node,index):
    taken[index]=True
    ret=node
    for i,item in enumerate(l):
        if not taken[i] and not ret.isdisjoint(item):
            ret.update(dfs(item,i))
    return ret

def merge_all():
    ret=[]
    for i,node in enumerate(l):
        if not taken[i]:
            ret.append(list(dfs(node,i)))
    return ret

print(merge_all())
