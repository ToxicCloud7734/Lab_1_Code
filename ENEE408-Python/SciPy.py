import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy.optimize import minimize
from scipy.fft import fft, fftfreq

print("3.4.1")
print(" ")

A = np.array([(3,1),(1,2)])
print(A)
print(" ")

B = np.array([9,8])
print(B)
print(" ")

x = linalg.solve(A,B)
print("Solution",x)

print(" ")
print("3.4.2")
print(" ")

def objective_function(x):
    return x**2 + 2*x

initial_guess = 0

result = minimize(objective_function, initial_guess)

print("Minimum x:", result.x[0])
print("Minimum y:", result.fun)

print(" ")
print("3.4.3")
print(" ")

fs = 1000  
T = 1 / fs 
N = 1000   
x = np.linspace(0, N*T, N, endpoint=False)
y = np.sin(100 * np.pi * x) + 0.5 * np.sin(160 * np.pi * x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]  # Only take positive frequencies

plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.title('Frequency Response of $f(x)$')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()