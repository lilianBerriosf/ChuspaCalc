BASES_SOPORTADAS = {2, 8, 10, 16}

DIGITOS_POR_BASE = {
    2: set("01"),
    8: set("01234567"),
    10: set("0123456789"),
    16: set("0123456789ABCDEF"),
}


def _validar_digitos(numero: str, base: int) -> None:
    cuerpo = numero[1:] if numero[:1] in "+-" else numero
    for caracter in cuerpo:
        if caracter not in DIGITOS_POR_BASE[base]:
            raise ValueError(f"Carácter inválido '{caracter}' para base {base}")


def convertir(numero: str, base_origen: int, base_destino: int) -> dict:
    """
    Convierte números entre bases 2, 8, 10 y 16.
    """

    if not numero or not numero.strip():
        raise ValueError("El número no puede estar vacío")

    if base_origen not in BASES_SOPORTADAS:
        raise ValueError(f"Base origen no soportada: {base_origen}")

    if base_destino not in BASES_SOPORTADAS:
        raise ValueError(f"Base destino no soportada: {base_destino}")

    numero = numero.strip().upper()

    _validar_digitos(numero, base_origen)

    try:
        valor_decimal = int(numero, base_origen)
    except ValueError as error:
        raise ValueError(
            f"Número inválido para base {base_origen}: {numero}"
        ) from error

    if base_destino == 2:
        resultado = bin(valor_decimal)[2:]
    elif base_destino == 8:
        resultado = oct(valor_decimal)[2:]
    elif base_destino == 10:
        resultado = str(valor_decimal)
    else:
        resultado = hex(valor_decimal)[2:].upper()

    return {
        "numero_original": numero,
        "base_origen": base_origen,
        "resultado": resultado,
        "base_destino": base_destino,
    }
