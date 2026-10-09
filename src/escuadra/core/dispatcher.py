"""
Despachador de comandos que mapea subcomandos a herramientas
consultando al registry real.
"""

import sys

from escuadra.core import registry

def dispatch(subcommand: str) -> int:
    """
    Despacha un subcomando a su herramienta correspondiente.

    Args:
        subcommand: Nombre del subcomando / herramienta a ejecutar.

    Returns:
        Código de salida entero (0 para éxito, 1 para error).
    """
    herramienta_cls = registry.buscar_por_nombre(subcommand)

    if herramienta_cls is None:
        print(
            f"Error: subcomando desconocido '{subcommand}'",
            file=sys.stderr,
        )
        return 1

    try:
        # Instanciamos la herramienta para validar que existe y es usable
        instancia = herramienta_cls()
        # Si tiene método de ejecución CLI, lo llamamos si existe
        if hasattr(instancia, "ejecutar"):
            instancia.ejecutar()
        elif hasattr(instancia, "run"):
            instancia.run()
        return 0
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1
    except Exception:
        return 1