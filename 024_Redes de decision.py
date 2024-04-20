# Importamos las bibliotecas necesarias
from sklearn.tree import DecisionTreeClassifier  # Importamos el clasificador de árbol de decisión
from sklearn.metrics import accuracy_score  # Importamos la métrica de precisión

# Creamos datos de ejemplo: tiempo de estudio en horas y horas de sueño
X = [[2, 8], [6, 9], [3, 5], [7, 6], [4, 7], [8, 2], [5, 3], [7, 4]]  # Lista de listas con tiempo de estudio y horas de sueño
y = ['Reprobar', 'Aprobar', 'Reprobar', 'Aprobar', 'Reprobar', 'Aprobar', 'Reprobar', 'Aprobar']  # Lista con etiquetas de clase

# Inicializamos el clasificador de árbol de decisión
clf = DecisionTreeClassifier()  # Creamos una instancia del clasificador de árbol de decisión

# Entrenamos el clasificador con los datos
clf.fit(X, y)  # Entrenamos el clasificador utilizando los datos de entrada X y las etiquetas y

# Creamos un nuevo dato de prueba
X_test = [[1, 2]]  # Creamos una lista de características para un nuevo dato de prueba

# Realizamos una predicción con el dato de prueba
prediction = clf.predict(X_test)  # Utilizamos el clasificador entrenado para predecir la clase del nuevo dato de prueba

# Imprimimos la predicción
print("Predicción:", prediction[0])  # Imprimimos la predicción de clase para el nuevo dato de prueba
