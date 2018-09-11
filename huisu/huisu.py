# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:33:29 2018
回溯法求出数组中任意个元素求和等于固定值的情况
@author: Will
"""
#l = int(input())
#a=[int(i) for i in input().split()]
#n = int(input())

n = 3

a = [1, 2, 0,-1,4]
x = []   # 一个解（n元0-1数组）
X = []   # 一组解
# 冲突检测：无
    
# 一个例子
# 冲突检测：和已有序列和>n则冲突，有相同元素则冲突
def conflict2(k):
    global n, x, X, a,i
    if sum(x[:k+1]) > n: 
        return True
    if i in x[:k]:
        return True
    if k==0:
        return False
    return False # 无冲突
   
# 子集树递归模板
def subsets(k): # 到达第k个元素
    global n, x, X, i
    if sum(x) == n:  # 求和目标值
        X.append(x[:])
 # 保存（一个解）
    else:
        for i in a: 
            x.append(i)
            if not conflict2(k): # 剪枝
                subsets(k+1)
            x.pop()            # 回溯    
subsets(0)
# 根据一个解x，构造一个子集
def get_a_subset(x):
    global a
    
    return [y[0] for y in filter(lambda s:s[1]!=0, zip(a,x))]

# 根据一组解X, 构造一组子集
def get_all_subset(X):
    return [get_a_subset(x) for x in X]

# 查看第3个解，及对应的子集
#print(X[2])
#print(get_a_subset(X[2]))

#print(get_all_subset(X))


