# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un modelo de Aprendizaje Inductivo usando Árboles de Regresión (M5).
# Utiliza la librería M5 en Python para entrenar un modelo de árbol de regresión y hacer predicciones.
#Comienza importando las librerías necesarias, incluyendo la implementación de M5 y funciones 
#auxiliares de sklearn. Luego, carga el conjunto de datos de Boston, lo divide en conjuntos de 
#entrenamiento y prueba, instancia el modelo M5, lo entrena con los datos de entrenamiento, realiza 
#predicciones sobre los datos de prueba y finalmente calcula el error cuadrático medio entre las 
#predicciones y los valores reales.

# Importamos las librerías necesarias
from m5 import M5Regression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Cargamos el conjunto de datos de Boston
boston = load_boston()
X = boston.data
y = boston.target

# Dividimos el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos una instancia del modelo de Árbol de Regresión M5
model = M5Regression()

# Entrenamos el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizamos predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Calculamos el error cuadrático medio entre las predicciones y los valores reales
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)
