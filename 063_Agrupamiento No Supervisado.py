# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de agrupamiento no supervisado utilizando el algoritmo K-Means. 
# Se generan datos aleatorios para dos grupos y se utiliza K-Means para agruparlos en función de su similitud.
# Importar las bibliotecas necesarias
import numpy as np  # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para visualización
from sklearn.cluster import KMeans  # Para el algoritmo K-Means

# Generar datos aleatorios para dos grupos
# Grupo 1: media en (1, 1) y desviación estándar de 0.6
X1 = np.random.normal(loc=[1, 1], scale=0.6, size=(100, 2))
# Grupo 2: media en (4, 4) y desviación estándar de 0.6
X2 = np.random.normal(loc=[4, 4], scale=0.6, size=(100, 2))

# Combinar los dos conjuntos de datos
X = np.concatenate((X1, X2), axis=0)

# Inicializar el modelo K-Means con 2 clusters
kmeans = KMeans(n_clusters=2)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Obtener las etiquetas de los grupos asignados por K-Means
labels = kmeans.labels_

# Obtener las coordenadas de los centroides de los grupos
centroids = kmeans.cluster_centers_

# Visualizar los datos y los centroides
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)  # Graficar los puntos de datos con colores según los grupos
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, c='red')  # Graficar los centroides
plt.title('Agrupamiento K-Means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
