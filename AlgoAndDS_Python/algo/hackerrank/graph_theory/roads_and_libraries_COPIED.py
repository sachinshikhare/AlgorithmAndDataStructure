"""
https://www.hackerrank.com/challenges/torque-and-development

COPIED. Not My Solution

3
3 3 2 1
1 2
3 1
2 3
6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6
6 6 5 2
1 3
3 4
2 4
1 2
2 3
5 6
"""

q = int(input().strip())
for a0 in range(q):
    # every query starting from scrach
    sets_flat = {}
    labels = {}
    val_map = {}
    result = 0
    cnt = 0

    a = input()
    n_cities,n_roads,cost_lib,cost_road = a.strip().split(' ')
    n_cities,n_roads,cost_lib,cost_road = [int(n_cities),int(n_roads),int(cost_lib),int(cost_road)]
    
    if n_roads == 0:
        print(n_cities*cost_lib)
        continue

    if cost_lib < cost_road:
        print(cost_lib*n_cities)
        
        # ingest and pass remaining inputs
        for a1 in range(n_roads):
            input()
        continue
    
    for a1 in range(n_roads):
        cnt += 1

        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        
        c1_label = sets_flat.get(city_1, None)
        c2_label = sets_flat.get(city_2, None)
        
        if (not c1_label) and (not c2_label):
            label = 'set_{}'.format(cnt)
            val = 'val_{}'.format(cnt)
            labels[label] = val

            sets_flat[city_1] = label
            sets_flat[city_2] = label

            val_map[val] = [label]
        
        elif (c1_label) and (not c2_label):
            sets_flat[city_2] = c1_label
        
        elif (not c1_label) and (c2_label):
            sets_flat[city_1] = c2_label
        
        elif labels[c1_label] == labels[c2_label]:
            continue
        
        elif labels[c1_label] != labels[c2_label]:
            val_map[labels[c1_label]].extend(val_map[labels[c2_label]])
            val_map.pop(labels[c2_label])
            
            for label in val_map[labels[c1_label]]:
                labels[label] = labels[c1_label]

        result += cost_road # +1 road

    # count libraries from merged sets
    result += (len(set(labels.values())))*cost_lib

    # add separated cities
    count_cities_in_sets = len(sets_flat)
    if count_cities_in_sets < n_cities:
        result += (cost_lib*(n_cities-count_cities_in_sets))

    print(result)