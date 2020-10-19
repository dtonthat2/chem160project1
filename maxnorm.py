import numpy as np
import matplotlib.pyplot as plt
N=200
ntrials=5000
mu=0.0
sd=1.0
arr=np.empty(N)
for i in range(1,201):
    avgmaxsum=0
    for j in range(ntrials):
        dist=np.random.normal(mu, sd, i)
        max=np.amax(dist)
        avgmaxsum+=max
    avgmax=avgmaxsum/ntrials
    arr[i-1]=avgmax
x=np.arange(1, 201).tolist()
plt.plot(x,arr)
plt.ylabel('Average maximum values')
plt.xlabel('Number of normally distributed random numbers')
plt.axis([0, 200, 0, 5])
plt.show()