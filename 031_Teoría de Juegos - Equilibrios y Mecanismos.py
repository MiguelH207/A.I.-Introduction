# Importamos la biblioteca numpy para realizar cálculos numéricos
import numpy as np

# Definimos una función para la subasta de segundo precio
def second_price_auction(bids):
    # Ordenamos las ofertas en orden descendente
    sorted_bids = np.sort(bids)[::-1]  # Ordena las ofertas de mayor a menor
    
    # El ganador es el que hizo la oferta más alta
    winner_index = np.where(bids == sorted_bids[0])[0][0]  # Encuentra el índice del ganador
    
    # El precio pagado es el segundo precio más alto
    second_price = sorted_bids[1] if len(sorted_bids) > 1 else 0  # Determina el segundo precio más alto
    
    return winner_index, second_price  # Retorna el índice del ganador y el segundo precio

# Ofertas de los jugadores en la subasta
bids = np.array([20, 30, 25, 15, 10])

# Ejecutamos la subasta y obtenemos el ganador y el precio pagado
winner_index, price_paid = second_price_auction(bids)

# Imprimimos el resultado de la subasta
print("El ganador de la subasta es el jugador", winner_index + 1)  # Ajusta el índice base 0 a base 1
print("El precio pagado por el ganador es", price_paid)
