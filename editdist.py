#!/usr/bin/env python
# coding=utf-8
# function   : calculate the minEditDistance of two strings


def minEditDist(sm,sn):
    #sm=seg_sentence(sm.replace(' ',''))
    #sn=seg_sentence(sn.replace(' ',''))

    m,n = len(sm)+1,len(sn)+1
    # create a matrix (m*n)
    matrix = [[0]*n for i in range(m)]
    matrix[0][0]=0
    for i in range(1,m):
        matrix[i][0] = matrix[i-1][0] + 1
    for j in range(1,n):
        matrix[0][j] = matrix[0][j-1]+1
    cost = 0
    for i in range(1,m):
        for j in range(1,n):
            if sm[i-1]==sn[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+cost)

    return matrix[m-1][n-1]
str1=unicode('你是傻逼对不对传','utf-8')
str2=unicode('艾伦•图灵传','utf-8')

  
mindist=minEditDist(str1,str2)
print mindist
print 1-float(mindist)/max(len(str1),len(str2))