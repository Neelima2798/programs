import math
def len_of_bldg_exp_sunlight(bldg_co,source_of_light):
    x_co = source_of_light[0]
    y_co = source_of_light[1]
    distances_from_light = dict()
    for i in range(len(bldg_co)):
        x1 =bldg_co[i][0]
        y1 =bldg_co[i][1]
        sqroot = math.sqrt( (x_co -x1)**2  + (y_co - y1)**2  )
        distances_from_light[sqroot] = bldg_co[i]
   
#     print(distances_from_light)
    removing_co = max(distances_from_light)
    keep_co = distances_from_light[min(distances_from_light)]
    x_1,y_1 = keep_co[0],keep_co[1]
#     print(x_1,y_1)
    del distances_from_light[removing_co]
    req_co = []
    for i in distances_from_light.values():
        req_co.append(i)
#     print(req_co)
    dis = []
    for i in range(len(req_co)):
        x1 = req_co[i][0]
        y1 = req_co[i][1]
#         print(x1,y1)
        if i !=keep_co:
            dis1 = math.sqrt( (x_1 - x1)**2 + (y_1 - y1)**2)    
            dis.append(dis1)
    print(sum(dis))
   
   
   
print(len_of_bldg_exp_sunlight([[4,0],[4,-5],[7,-5],[7,0]] ,[1,1] ))
