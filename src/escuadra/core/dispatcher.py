"""
Despachador de comandos que mapea subcomandos a herramientas
consultando al registry real.
"""

from __future__ import annotations

import sys
from typing import Any

from escuadra.core.registry import buscar_por_nombre

def despacho(nombre: str) -> Any:
    """Despacha un subcomando a su herramienta."""
    herramienta_cls = buscar_por_nombre(nombre)

    if herramienta_cls is None:
        print(
            f"Error: subcomando desconocido '{nombre}'",
            file=sys.stderr,
        )
        return None

    instancia = herramienta_cls()

    if hasattr(instancia, "ejecutar"):
        return instancia.ejecutar()
    if hasattr(instancia, "run"):
        return instancia.run()

    return instancia

def dispatch(subcommand: str) -> int:
    """
    Despacha un subcomando a su herramienta correspondiente.

    Args:
        subcommand: Nombre del subcomando / herramienta a ejecutar.

    Returns:
        Código de salida entero (0 para éxito, 1 para error).
    """
    result = despacho(subcommand)

    if result is None:
        return 1

    try:
        if isinstance(result, int):
            return result
        return 0
    except Exception as exc:
        print(f"Error ejecutando '{subcommand}': {exc}", file=sys.stderr)
        return 1    if hasattr(instancia, "ejecutar"):
           return instancia.ejecutar()
        elif hasattr(instancia, "run"):
            return instancia.run()
        return 0
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1
    except Exception:
        return 1
