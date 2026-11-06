"""
Funciones de matemática financiera básica.
"""


def calcular_valor_futuro(valor_presente: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor futuro usando interés compuesto.

    VF = VP * (1 + i) ** n
    """
    return valor_presente * (1 + tasa) ** periodos


def calcular_valor_presente(valor_futuro: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor presente.

    VP = VF / (1 + i) ** n
    """
    return valor_futuro / (1 + tasa) ** periodos


def calcular_interes_compuesto(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula únicamente el interés ganado.

    I = VF - Capital
    """
    valor_futuro = calcular_valor_futuro(capital, tasa, periodos)
    return valor_futuro - capital


def _validar_parametros(capital: float, tasa: float, periodos: int) -> None:
    """
    Verifica que capital >= 0, tasa >= 0 y periodos > 0.

    Raises:
        ValueError: Si alguno de los valores es inválido (incluido NaN).
    """
    if not capital >= 0:
        raise ValueError(
            f"capital debe ser mayor o igual que 0. Se recibió: {capital}."
        )
    if not tasa >= 0:
        raise ValueError(
            f"tasa debe ser mayor o igual que 0. Se recibió: {tasa}."
        )
    if not periodos > 0:
        raise ValueError(
            f"periodos debe ser mayor que 0. Se recibió: {periodos}."
        )


def calcular_interes_simple(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula el interés simple.

    I = Capital * i * n

    Raises:
        ValueError: Si capital < 0, tasa < 0 o periodos <= 0.
    """
    _validar_parametros(capital, tasa, periodos)
    return capital * tasa * periodos


def calcular_cuota_prestamo(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula la cuota nivelada de un préstamo (sistema francés).

    C = Capital * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    Con tasa 0 la fórmula no está definida (división entre cero), por lo que
    la cuota es Capital / n.

    Raises:
        ValueError: Si capital < 0, tasa < 0 o periodos <= 0.
    """
    _validar_parametros(capital, tasa, periodos)

    if tasa == 0:
        return capital / periodos

    factor = (1 + tasa) ** periodos
    return capital * (tasa * factor) / (factor - 1)
