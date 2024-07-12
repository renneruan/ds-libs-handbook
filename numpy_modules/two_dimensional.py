# %%
import numpy as np

#%%
a = np.array([[11,12,13],[21,22,23],[31,32,33]])
print(a)
# %%

x1 = np.array([[0,1],[1,0]])
x2 = np.array([[3,1],[1,2]])

print(x1 + x2)
print(x1 * x2)
print(x1 + 2)

# %%
a = np.array([[0,1,1],[1,0,1]])
b = np.array([[1,1],[1,1],[-1,1]])

print (np.dot(a,b))