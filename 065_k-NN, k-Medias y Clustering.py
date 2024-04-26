# Miguel Angel Huerta Castillo     21310236
# Este programa implementa algoritmos de aprendizaje probabilístico: k-NN (k-Vecinos más Cercanos), k-Medias y Clustering.
# El k-NN clasifica un nuevo punto basado en la mayoría de los k puntos más cercanos.
# El k-Medias agrupa puntos en k clusters, minimizando la distancia intra-cluster.
# El Clustering agrupa puntos en clusters basados en similitud, sin necesidad de etiquetas previas.

import numpy as np  # Importa la biblioteca NumPy para operaciones matemáticas eficientes
from sklearn.datasets import make_blobs  # Importa la función make_blobs para generar datos de prueba
from sklearn.model_selection import train_test_split  # Importa la función train_test_split para dividir datos en conjuntos de entrenamiento y prueba
from sklearn.neighbors import KNeighborsClassifier  # Importa el clasificador de k-NN de scikit-learn
from sklearn.cluster import KMeans  # Importa el algoritmo de k-Medias de scikit-learn
from sklearn.cluster import AgglomerativeClustering  # Importa el algoritmo de Clustering de scikit-learn

# Genera datos de prueba con 500 muestras, 2 características y 4 centroides
X, y = make_blobs(n_samples=500, centers=4, n_features=2, random_state=42)

# Divide los datos generados en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un clasificador de k-NN con k=5
knn = KNeighborsClassifier(n_neighbors=5)

# Entrena el clasificador de k-NN con los datos de entrenamiento
knn.fit(X_train, y_train)

# Evalúa el clasificador de k-NN con los datos de prueba
accuracy_knn = knn.score(X_test, y_test)
print("Accuracy k-NN:", accuracy_knn)

# Crea un modelo de k-Medias con 4 clusters
kmeans = KMeans(n_clusters=4)

# Entrena el modelo de k-Medias con los datos de entrenamiento
kmeans.fit(X_train)

# Predice los clusters de los datos de prueba
y_kmeans = kmeans.predict(X_test)

# Calcula la precisión del modelo de k-Medias
accuracy_kmeans = np.mean(y_kmeans == y_test)
print("Accuracy k-Means:", accuracy_kmeans)

# Crea un modelo de Clustering con 4 clusters usando enlace completo (complete linkage)
clustering = AgglomerativeClustering(n_clusters=4, linkage='complete')

# Entrena el modelo de Clustering con los datos de entrenamiento
clustering.fit(X_train)

# Predice los clusters de los datos de prueba
y_clustering = clustering.fit_predict(X_test)

# Calcula la precisión del modelo de Clustering
accuracy_clustering = np.mean(y_clustering == y_test)
print("Accuracy Clustering:", accuracy_clustering)
