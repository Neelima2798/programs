def checking_point_in_polygon(x_co,y_co,polygon):

    len_of_poly = len(polygon)
    inside =False

    x1,y1 = polygon[0]
    for i in range(len_of_poly+1):
        x2,y2 = polygon[i % len_of_poly]
        if y_co > min(y1,y2):
            if y_co <= max(y1,y2):
                if x_co <= max(x1,x2):
                    if y1 != y2:
                        xinters = (y_co-y1)*(x2-x1)/(y2-y1)+x1
                    if x1 == x2 or x_co <= xinters:
                        inside = not inside
        x1,y1 = x2,y2

    return inside

print(checking_point_in_polygon(4,1,[[1,0],[8,3],[8,8],[1,5]]))
print(checking_point_in_polygon(3,4,[[1,0],[8,3],[8,8],[1,5]]))
print(checking_point_in_polygon(4,6,[[2,0],[5,3],[7,8],[1,3]]))
