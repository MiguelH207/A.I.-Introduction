# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un modelo de Aprendizaje Probabilístico utilizando Máquinas de Vectores Soporte (SVM) con un núcleo específico.
# Se utiliza un conjunto de datos de ejemplo para entrenar el modelo y luego realizar predicciones sobre datos de prueba.

# Importamos las bibliotecas necesarias
import numpy as np  # Importamos NumPy para manipulación numérica
from sklearn import datasets  # Importamos datasets de sklearn para obtener conjuntos de datos de ejemplo
from sklearn.model_selection import train_test_split  # Importamos train_test_split para dividir el conjunto de datos en entrenamiento y prueba
from sklearn.svm import SVC  # Importamos SVC (Support Vector Classification) para implementar SVM

# Cargamos un conjunto de datos de ejemplo (iris dataset)
iris = datasets.load_iris()

# Dividimos el conjunto de datos en características (X) y etiquetas (y)
X = iris.data
y = iris.target

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Creamos un clasificador SVM con un kernel gaussiano (RBF)
classifier = SVC(kernel='rbf')

# Entrenamos el clasificador utilizando los datos de entrenamiento
classifier.fit(X_train, y_train)

# Realizamos predicciones sobre los datos de prueba
y_pred = classifier.predict(X_test)

# Calculamos la precisión del modelo
accuracy = np.mean(y_pred == y_test)

# Imprimimos la precisión del modelo
print("Accuracy:", accuracy)
