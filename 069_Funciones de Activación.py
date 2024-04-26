# Miguel Angel Huerta Castillo     21310236

# Este programa implementa una red neuronal simple en Python utilizando la biblioteca de TensorFlow. 
# La red neuronal tiene una capa oculta con una función de activación ReLU y una capa de salida con una función de activación softmax.
# Se utiliza un conjunto de datos de ejemplo de clasificación de flores Iris para entrenar la red neuronal.
# El programa está comentado línea por línea para explicar qué hace cada parte del código.

# Importar las bibliotecas necesarias
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Codificar las etiquetas utilizando One-Hot Encoding
encoder = OneHotEncoder(categories='auto')
y_train = encoder.fit_transform(y_train.reshape(-1, 1)).toarray()
y_test = encoder.transform(y_test.reshape(-1, 1)).toarray()

# Definir los parámetros de la red neuronal
input_size = 4
hidden_layer_size = 8
output_size = 3

# Crear el modelo de la red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Dense(hidden_layer_size, activation='relu', input_shape=(input_size,)), # Capa oculta con activación ReLU
    tf.keras.layers.Dense(output_size, activation='softmax') # Capa de salida con activación softmax
])

# Compilar el modelo especificando la función de pérdida y el optimizador
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo utilizando los datos de entrenamiento
model.fit(X_train, y_train, epochs=100, batch_size=8, verbose=1)

# Evaluar el modelo utilizando los datos de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)

# Imprimir la precisión del modelo en los datos de prueba
print("Accuracy:", test_acc)
