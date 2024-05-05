# Miguel Angel Huerta Castillo     21310236
# Este programa implementa el algoritmo de Boosting para Aprendizaje Inductivo.
# Boosting es una técnica de conjunto que combina múltiples modelos débiles para crear un modelo fuerte.
# En este ejemplo, se utiliza Boosting para predecir la clase de flores Iris en función de sus características.

from sklearn.datasets import load_iris  # Importa la función para cargar el conjunto de datos de iris
from sklearn.model_selection import train_test_split  # Importa la función para dividir el conjunto de datos en entrenamiento y prueba
from sklearn.ensemble import AdaBoostClassifier  # Importa el clasificador AdaBoost
from sklearn.metrics import accuracy_score  # Importa la métrica de precisión

# Cargar el conjunto de datos de iris
iris = load_iris()

# Dividir el conjunto de datos en características (X) y etiquetas (y)
X = iris.data
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el clasificador AdaBoost con un estimador base (DecisionTreeClassifier en este caso)
clf = AdaBoostClassifier()

# Entrenar el clasificador AdaBoost
clf.fit(X_train, y_train)

# Predecir las etiquetas en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión de las predicciones
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión
print("Accuracy:", accuracy)
