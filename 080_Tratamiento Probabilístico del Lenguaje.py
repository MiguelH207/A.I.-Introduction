# Miguel Angel Huerta Castillo     21310236
# Este programa realiza extracción de información mediante técnicas probabilísticas del lenguaje.
# Utiliza la biblioteca SpaCy para realizar el procesamiento del lenguaje natural.

import spacy  # Importa la biblioteca SpaCy

# Carga el modelo de lenguaje en español de SpaCy
nlp = spacy.load("es_core_news_sm")

# Define una función para extraer entidades nombradas de un texto utilizando SpaCy
def extract_entities(text):
    doc = nlp(text)  # Procesa el texto con el modelo de lenguaje de SpaCy
    entities = [ent.text for ent in doc.ents if ent.label_ in ["PER", "LOC", "ORG"]]  # Filtra las entidades nombradas relevantes
    return entities

# Texto de ejemplo en español
sample_text = "El presidente Andrés Manuel López Obrador habló sobre el cambio climático en la Cumbre de la Tierra."

# Extrae entidades nombradas del texto de ejemplo
extracted_entities = extract_entities(sample_text)

# Imprime las entidades extraídas
print("Entidades nombradas:")
for entity in extracted_entities:
    print(entity)
