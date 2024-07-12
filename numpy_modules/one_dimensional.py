# %%

import numpy as np

a = np.array([1,2,3,4,5])

print(type(a))

print(f'Size {a.size}')
print(f'Dimensions {a.ndim}')

# %%
a[3:5] = 100,200
print(a)
# %%
u = np.array([0,1])
v = np.array([1,0])

z = u + v
print(z)
# %%
y = np.array([1,2])
multiplied_y = y * 2
print(multiplied_y)
# %%

v1 = np.array([2,3])
u1 = np.array([3,1])

z1 = v1 * u1
print(z1)
#%%

a1 = np.array([2,3,3])
b1 = np.array([3,1,4])

c1 = np.dot(a1,b1)
print(c1)
# %%
u = np.array([1,2,3,-1])
u = u + 1
print(u)
# %%
x = np.array([0,np.pi/2, np.pi])
y = np.sin(x)
print(y) 

# %%
np.linspace(-2,2,num=9)
# %%
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x,y)