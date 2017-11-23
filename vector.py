#author: Anurag Kulshrestha
#company: IIRS
#Date of project underataken: 8-1-2017
#Date of completion: 12-1-2017
#This program is designed to do some basic vector geo-data processing such as finding distance between co-ordinates, checking intersecting lines, points inside polygons, etc.
#Note: Please do not share without proper consent of the author
#change_1

import math
import matplotlib.pyplot as plt
from matplotlib import collections as mc

def p_distance(p1,p2):
    x1,y1,x2,y2=p1[0],p1[1],p2[0],p2[1]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
    #print x1

def s_length(lineseg):
    beg=lineseg[0]
    end=lineseg[1]
    return p_distance(beg,end)

def l_length(line):
    result=0
    for i in range(0,len(line)-1):
        result=result+p_distance(line[i],line[i+1])
    return result

def slope(beg,end):
    return (beg[1]-end[1])/float(beg[0]-end[0])

def eqn(m,p1,p_check):
    y_check,x_check,y1,x1=p_check[1], p_check[0],p1[1],p1[0]
    v=(y_check-y1)-m*(x_check-x1)
    return v

def end_point_crossing(line1,line2):
    slope1=slope(line1[0],line1[1])
    p1=line1[0]
    v1=eqn(slope1,p1,line2[0])
    v2=eqn(slope1,p1,line2[1])
    if(v1==0 and v2!=0):
        return line2[0]
    elif(v1!=0 and v2==0):
        return line2[1]

def s_areCrossingOne(line1,line2):
    slope1=slope(line1[0],line1[1])
    p1=line1[0]
    v1=eqn(slope1,p1,line2[0])
    v2=eqn(slope1,p1,line2[1])
    if((v1<0 and v2<0)or(v1>0 and v2>0)):
        return False
    elif(v1==0 and v2==0):
        return False
    else:
        return True

def s_areCrossing(line1, line2):
    if(s_areCrossingOne(line1,line2) and s_areCrossingOne(line2,line1)):
        return True
    else:
        return False

def line_to_lineseg(line):
    result=[]
    for i in range(0,len(line)-1):
        result.append([line[i],line[i+1]])
    return result
    
def l_selfIntersect(line):
    for i in range(0,len(line)-1):
        for j in range(0,len(line)-1):
            if(s_areCrossing([line[i],line[i+1]],[line[j],line[j+1]]) and abs(i-j)>1):
                return True
            else:
                continue
    return False

def l_isClosed(line):
    length=len(line)
    if(line[0][0]==line[length-1][0] and line[0][1]==line[length-1][1]):
        return True
    else:
        return False

def countIntersects(lineseg, poly):
    count=0
    if(l_isClosed(poly)):
        seg=line_to_lineseg(poly)
        for i in seg:
            if(s_areCrossing(i,lineseg)):
                count+=1
            if((end_point_crossing(lineseg,i) in poly)):
                count-=0.5
    return count
    
def p_inPolygon(p,poly):
    #test=float("inf")
    lineseg=[p,[1000,1000]]
    if(countIntersects(lineseg,poly)%2==0):
        return False
    else:
        return True

def pol_contains(poly1,poly2):#if poly1 inside poly2
    for i in poly1:
       if(p_inPolygon(i,poly2)==False):
           return False
    return True
           
    
    
def plot_line_seg():
    line1,line2=[1,2,1,1.5,1],[6,10,10,9.5,6]
    line3,line4=[.5,.7,2.5,2,0,.5],[8,11,11.5,4,4,8]
    plt.plot(line1,line2)
    plt.plot(line3,line4)
    plt.plot([1.5],[6],'ro')
    plt.plot([0.5,2],[9,10])
    plt.axis([0,4,0,12])
    plt.show()


if __name__=='__main__':
    poly=[[1,6],[2,10],[1,10],[1.5,9.5],[1,6]]
    poly1=[[0.5,8],[.7,11],[2.5,11.5],[2,4],[0,4],[.5,8]]
    line2=[[1,6],[2,10],[1,10],[1.5,9.5]]
    lineseg=[[.5,9],[2,10]]
    point=[1.5,6]
    #print(p_distance([1,1],[2,2]))
    #print(s_areCrossing([[1,8],[2,12]],[[1,10],[1.5,9.5]]))
    #print(s_areCrossing([[1,10],[1.5,9.5]],[[1,6],[2,10]]))
    #print(l_selfIntersect(poly))
    #print(line_to_lineseg(poly))
    #print(l_isClosed(line1))
    #print(p_inPolygon(point,poly))
    #print(p_inPolygon(point,poly1))
    #print(pol_contains(poly,poly1))
    #print(countIntersects(lineseg1,poly))
    plot_line_seg()
