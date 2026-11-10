from pathlib import Path


def formatear_numero(valor, decimales=2):
    """
    Formatea un número con separadores de miles.
    """
    if decimales == 0:
        return f"{valor:,.0f}"

    return f"{valor:,.{decimales}f}"


def copiar_al_portapapeles(texto):
    """
    Copia texto al portapapeles.
    """
    from PySide6.QtWidgets import QApplication
    app = QApplication.instance()

    if app is None:
        raise RuntimeError("No hay QApplication activa")

    clipboard = app.clipboard()
    clipboard.setText(texto)


def exportar_a_archivo(contenido, ruta):
    """
    Exporta contenido a un archivo.
    """
    path = Path(ruta)

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def leer_archivo(ruta):
    """
    Lee un archivo y devuelve su contenido.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


def validar_numero(texto, permitir_negativo=True, permitir_decimal=True):
    """
    Valida si un texto puede convertirse a número.
    """
    try:
        numero = float(texto)

        if not permitir_negativo and numero < 0:
            return False

        if not permitir_decimal and "." in texto:
            return False

        return True

    except ValueError:
        return False
