import numpy as np
print("3.2.3")
print(" ")
a = np.array([(1,2,3,4)])


print(a)
print(" ")
print("3.2.4")
print(" ")
b = np.ones((3,4))
print(b)

print(" ")

c = np.zeros((4,3))
print(c) 
print(" ")
print("3.2.5")
print(" ")
print("Matrix A")
A = np.array([(1,2,3),(4,5,6)])
print(A)

print(" ")

print("Matrix B")
B = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print(B)

print(" ")

print("Matrix AxB")
print(A@B)
print(" ")
print("3.2.6")
print(" ")
c = np.array([(3,1),(1,2)])
print(c)
print(" ")
print(np.linalg.eig(c))