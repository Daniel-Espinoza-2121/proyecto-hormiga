from hierba import hierba
from azucar import azucar
from vino import vino
from veneno import veneno
from roca import roca

class Laberinto:
    def __init__(self, canvas, size):
        self.canvas = canvas
        self.size = size
        self.matriz = [[hierba(self.canvas, 15 + 30 * i, 15 + 30 * j) for i in range(size)] for j in range(size)]

    def crear(self, num, x, y):
        """Crea un ítem en las coordenadas (x, y) y lo coloca en la matriz."""
        tipos_de_item = {
            0: hierba,
            1: azucar,
            2: vino,
            3: veneno,
            4: roca
        }
        item_clase = tipos_de_item[num]
        item = item_clase(self.canvas, 15 + 30 * x, 15 + 30 * y)
        self.matriz[y][x] = item
        return item

    def reemplazar(self, num, x, y):
        """Elimina el ítem en la posición (x, y) y lo reemplaza."""
        # Elimina la imagen del ítem del Canvas
        self.canvas.delete(self.matriz[y][x].id)
        # Reemplaza el ítem eliminado con una instancia de Hierba
        self.matriz[y][x] = self.crear(num, x, y)
        self.canvas.update()


