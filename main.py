import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

# Parametreler
r = 3.9  # Kaotik davranış gösteren bir değer seçebilirsiniz
x0 = 0.1  # Başlangıç değeri

# İterasyon sayısı
iterations = 1000

# Değerleri saklamak için dizi
values = np.zeros(iterations+1)
values[0] = x0

# İterasyonları yap
for i in range(iterations):
    values[i+1] = logistic_map(r, values[i])

# Sonuçları çiz
plt.plot(values, 'b-', lw=0.5)
plt.title('Logistic Map')
plt.xlabel('İterasyon')
plt.ylabel('Değer')
plt.show()
