l = [1,2,3,4,4,5,5,6,1,2,6,7,6,8,7]
print(set([x for x in l if l.count(x) > 1]))
