from datetime import datetime


class Historial:
    """
    Historial en memoria de los últimos 20 cálculos realizados.
    """

    LIMITE = 20

    def __init__(self):
        self._historial = []

    def agregar_calculo(
        self,
        herramienta: str,
        parametros: dict,
        resultado: dict,
    ) -> None:
        """
        Agrega un cálculo al historial con timestamp.
        """
        entrada = {
            "timestamp": datetime.now().isoformat(),
            "herramienta": herramienta,
            "parametros": parametros,
            "resultado": resultado,
        }

        self._historial.append(entrada)

        if len(self._historial) > self.LIMITE:
            self._historial.pop(0)

    def editar_nota(self, timestamp: str, nota: str) -> bool:
        """
        Actualiza la nota de una entrada identificada por su timestamp.

        Args:
            timestamp: Marca de tiempo de la entrada que se editará.
            nota: Texto de la nueva nota.

        Returns:
            True si se actualizó la nota; False si la entrada no existe.
        """
        for entrada in self._historial:
            if entrada["timestamp"] == timestamp:
                entrada["nota"] = nota
                return True

        return False

    def obtener_historial(self) -> list:
        """
        Retorna el historial más reciente primero.
        """
        return list(reversed(self._historial))

    def obtener_ultimo(self) -> dict | None:
        """
        Retorna el último registro o None si está vacío.
        """
        if not self._historial:
            return None

        return self._historial[-1]

    def limpiar(self) -> None:
        """
        Vacía el historial.
        """
        self._historial.clear()
