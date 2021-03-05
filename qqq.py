import numpy as np
a = ((1,2),(3,4),(5,6))
c = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
b = np.float32([c[i] for (_, i) in a])
print(b)