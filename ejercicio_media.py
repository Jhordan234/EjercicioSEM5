import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [5, 7, 8, 12, 15, 17, 18, 20, 21, 25, 30, 35]

# Calcular la media y la mediana
media = np.mean(datos)
mediana = np.median(datos)

# Crear un gráfico
plt.figure(figsize=(8, 6))
plt.hist(datos, bins=7, edgecolor='black', alpha=0.7)

# Añadir líneas para la media y mediana
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media}')
plt.axvline(mediana, color='blue', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana}')

# Etiquetas y título
plt.title('Distribución de los Datos con Media y Mediana')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()

# Mostrar gráfico
plt.show()