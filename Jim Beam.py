#!/bin/python3

import os
import sys

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
        px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        return [px, py]

def find_slop(x1,y1,x2,y2):
    if(x1!=x2):
        return (y2-y1)/(x2-x1)
    else:
        return 818.818

def solve(x1, y1, x2, y2, xm, ym):
    slop_1=find_slop(x1,y1,x2,y2)
    slop_2=find_slop(0,0,xm,ym)
    #print(slop_1,slop_2)

    if(slop_1==slop_2):
        if(slop_1!=1):
            res="YES"
        else:
            if(xm<min(x1,x2)):
                res="YES"
            else:
                res="NO"
    else:
        point=findIntersection(x1,y1,x2,y2,0,0,xm,ym)
        print(point)
        if(point[0]<=max(x1,x2) and point[0]>=min(x1,x2) and point[1]<=max(y1,y2) and point[1]>=min(y1,y2) and point[0]<=max(0,xm) and point[0]>=min(0,xm) and point[1]<=max(0,ym) and point[1]>=min(0,ym)):
            res="NO"
        else:
            res="YES"
        #res="bb"
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        x1Y1X2Y2XmYm = input().split()

        x1 = int(x1Y1X2Y2XmYm[0])

        y1 = int(x1Y1X2Y2XmYm[1])

        x2 = int(x1Y1X2Y2XmYm[2])

        y2 = int(x1Y1X2Y2XmYm[3])

        xm = int(x1Y1X2Y2XmYm[4])

        ym = int(x1Y1X2Y2XmYm[5])

        result = solve(x1, y1, x2, y2, xm, ym)

        fptr.write(result + '\n')

    fptr.close()
