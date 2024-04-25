# Miguel Angel Huerta Castillo     21310236
# Este programa realiza un reconocimiento del habla para solicitar al usuario que ingrese una frase. Luego, utiliza el reconocimiento probabilístico para determinar si el usuario ha dicho "sí" o "no" en respuesta a una pregunta específica.
# Importamos la librería para el reconocimiento de voz
import speech_recognition as sr

# Función para reconocimiento de voz
def reconocer_voz():
    # Inicializamos el reconocedor de voz
    reconocedor = sr.Recognizer()
    
    # Abrimos el micrófono para escuchar al usuario
    with sr.Microphone() as source:
        print("Diga algo:")
        # Escuchamos al usuario y almacenamos el audio
        audio = reconocedor.listen(source)
    
    try:
        print("Reconociendo...")
        # Utilizamos el reconocedor para convertir el audio en texto
        texto = reconocedor.recognize_google(audio, language='es-ES')
        print("Has dicho: " + texto)
        # Devolvemos el texto reconocido
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print("Error en la solicitud: {0}".format(e))
        return ""

# Función principal
def main():
    # Preguntamos al usuario si está de acuerdo
    print("¿Estás de acuerdo? Responde sí o no.")
    # Llamamos a la función de reconocimiento de voz para obtener la respuesta del usuario
    respuesta = reconocer_voz()
    
    # Si la respuesta es "sí" o "si", mostramos un mensaje de acuerdo
    if "sí" in respuesta.lower() or "si" in respuesta.lower():
        print("Estás de acuerdo.")
    # Si la respuesta es "no", mostramos un mensaje de desacuerdo
    elif "no" in respuesta.lower():
        print("No estás de acuerdo.")
    # Si la respuesta no se pudo entender, solicitamos al usuario que responda de nuevo
    else:
        print("No se pudo entender tu respuesta. Por favor, responde nuevamente.")

# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
