# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un clasificador de texto usando Aprendizaje Bayesiano.
# El programa entrena un modelo de Aprendizaje Bayesiano con un conjunto de datos de ejemplos etiquetados.
# Luego, utiliza este modelo para predecir la clase de nuevas instancias de texto.

from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self, classes):
        self.classes = classes
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_counts = defaultdict(int)
        self.vocabulary = set()

    def train(self, X, y):
        for xi, yi in zip(X, y):
            for word in xi.split():
                self.class_word_counts[yi][word] += 1
                self.class_counts[yi] += 1
                self.vocabulary.add(word)

    def predict(self, X):
        predictions = []
        for xi in X:
            max_prob = float('-inf')
            best_class = None
            for c in self.classes:
                log_prob = 0
                for word in xi.split():
                    log_prob += (self.class_word_counts[c][word] + 1) / (self.class_counts[c] + len(self.vocabulary))
                log_prob += self.class_counts[c]
                if log_prob > max_prob:
                    max_prob = log_prob
                    best_class = c
            predictions.append(best_class)
        return predictions

# Ejemplo de uso del clasificador
# Datos de entrenamiento
X_train = ["me gusta jugar futbol", "me gusta leer libros", "no me gusta el futbol"]
y_train = ["deporte", "lectura", "deporte"]

# Crear y entrenar el clasificador
classifier = NaiveBayesClassifier(classes=["deporte", "lectura"])
classifier.train(X_train, y_train)

# Datos de prueba
X_test = ["me gusta el futbol", "me gusta leer"]

# Predecir clases de los datos de prueba
predictions = classifier.predict(X_test)
print(predictions)  # Salida esperada: ['deporte', 'lectura']
