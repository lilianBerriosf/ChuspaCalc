
import math
from numbers import Real


def calcular_discriminante(a, b, c):
    """
    Calcula el discriminante de una ecuación cuadrática.

    Fórmula:
        D = b**2 - 4*a*c

    Args:
        a: Coeficiente cuadrático, distinto de cero.
        b: Coeficiente lineal.
        c: Término independiente.

    Returns:
        float: Valor del discriminante.

    Raises:
        ValueError: Si los coeficientes son inválidos.
    """

    coeficientes = (a, b, c)

    for coeficiente in coeficientes:
        if (
            isinstance(coeficiente, bool)
            or not isinstance(coeficiente, Real)
            or not math.isfinite(coeficiente)
        ):
            raise ValueError("Los coeficientes deben ser números reales finitos.")

    if a == 0:
        raise ValueError("El coeficiente a no puede ser cero.")

    discriminante = b**2 - 4 * a * c

    if not math.isfinite(discriminante):
        raise ValueError("El discriminante calculado no es finito.")

    return discriminante
