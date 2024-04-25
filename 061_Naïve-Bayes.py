# Miguel Angel Huerta Castillo     21310236
# Programa de Aprendizaje Probabilístico usando Naïve-Bayes
# Este programa implementa un clasificador Naïve-Bayes para predecir la clase de un conjunto de datos.
# Funciona calculando las probabilidades condicionales de las características dado cada clase y utiliza estas probabilidades para hacer predicciones.

import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features = X.shape # Obtiene el número de muestras y características del conjunto de datos
        self.classes = np.unique(y) # Obtiene las clases únicas en el conjunto de etiquetas
        n_classes = len(self.classes) # Obtiene el número de clases

        # Inicializa diccionarios para almacenar las estadísticas
        self.mean = {}
        self.var = {}
        self.priors = {}

        for c in self.classes:
            X_c = X[y == c] # Filtra las muestras correspondientes a la clase c
            self.mean[c] = np.mean(X_c, axis=0) # Calcula la media de cada característica para la clase c
            self.var[c] = np.var(X_c, axis=0) # Calcula la varianza de cada característica para la clase c
            self.priors[c] = len(X_c) / n_samples # Calcula la probabilidad a priori de la clase c

    def predict(self, X):
        y_pred = [self._predict(x) for x in X] # Realiza la predicción para cada muestra en X
        return np.array(y_pred)

    def _predict(self, x):
        posteriors = []

        # Calcula la probabilidad posterior para cada clase
        for c in self.classes:
            prior = np.log(self.priors[c]) # Calcula el logaritmo de la probabilidad a priori de la clase c
            posterior = np.sum(np.log(self._pdf(c, x))) # Calcula el logaritmo de la función de densidad de probabilidad para la clase c
            posterior = prior + posterior # Suma el logaritmo de la probabilidad a priori y el logaritmo de la función de densidad de probabilidad
            posteriors.append(posterior) # Agrega la probabilidad posterior a la lista de posteriores

        return self.classes[np.argmax(posteriors)] # Devuelve la clase con la mayor probabilidad posterior

    def _pdf(self, class_, x):
        mean = self.mean[class_] # Obtiene la media para la clase dada
        var = self.var[class_] # Obtiene la varianza para la clase dada
        numerator = np.exp(-((x - mean) ** 2) / (2 * var)) # Calcula el numerador de la función de densidad de probabilidad
        denominator = np.sqrt(2 * np.pi * var) # Calcula el denominador de la función de densidad de probabilidad
        return numerator / denominator # Devuelve la función de densidad de probabilidad

# Ejemplo de uso del clasificador Naïve-Bayes
if __name__ == "__main__":
    # Conjunto de datos de ejemplo
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    y = np.array([0, 0, 1, 1, 2, 2])

    # Crear y entrenar el modelo Naïve-Bayes
    model = NaiveBayes()
    model.fit(X, y)

    # Datos de prueba
    X_test = np.array([[2, 3], [5, 6]])

    # Realizar predicciones
    predictions = model.predict(X_test)

    # Imprimir predicciones
    print("Predicciones:", predictions)
