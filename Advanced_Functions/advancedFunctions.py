import math
l = [i for i in range(10)]
k = [i*i for i in range(10)]

mapped_list = list(map(lambda x,y: math.sqrt(y), l, k))
print(mapped_list)


