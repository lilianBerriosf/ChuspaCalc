import math

import pytest

from escuadra.modulos.matematicas.conversor_angulo import (
    convertir_angulo,
    grados_a_dms,
    grados_a_radianes,
    radianes_a_grados,
)


def test_grados_a_radianes_180():
    assert grados_a_radianes(180.0) == pytest.approx(math.pi)


def test_radianes_a_grados_pi():
    assert radianes_a_grados(math.pi) == pytest.approx(180.0)


def test_grados_a_dms_45_5():
    grados, minutos, segundos = grados_a_dms(45.5)

    assert grados == 45
    assert minutos == 30
    assert segundos == pytest.approx(0.0)


def test_convertir_angulo_100_gradianes_a_grados():
    assert convertir_angulo(100, "gradianes", "grados") == pytest.approx(90.0)


@pytest.mark.parametrize(
    "valor",
    [float("nan"), float("inf"), float("-inf")],
)
def test_funciones_angulo_rechazan_valores_no_finitos(valor):
    with pytest.raises(ValueError):
        grados_a_radianes(valor)

    with pytest.raises(ValueError):
        radianes_a_grados(valor)

    with pytest.raises(ValueError):
        grados_a_dms(valor)

    with pytest.raises(ValueError):
        convertir_angulo(valor, "grados", "radianes")


def test_funciones_angulo_rechazan_valores_no_numericos():
    with pytest.raises(ValueError):
        grados_a_radianes("180")
