import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lorenz_system(state, t, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parametreler
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Başlangıç koşulları
initial_state = [1.0, 1.0, 1.0]

# Zaman aralığı
t = np.linspace(0, 50, 10000)

# Diferansiyel denklemleri çöz
solution = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))

# Çözümü çiz
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='x(t)')
plt.plot(t, solution[:, 1], label='y(t)')
plt.plot(t, solution[:, 2], label='z(t)')
plt.title('Lorenz Sistemi Çözümü')
plt.xlabel('Zaman')
plt.ylabel('Değer')
plt.legend()
plt.grid()
plt.show()
