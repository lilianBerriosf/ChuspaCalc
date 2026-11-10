"""
Despachador de comandos que mapea subcomandos a funciones ejecutables
consultando dinámicamente al registry.
"""

import importlib
import sys

from chuspacalc.core import registry


def _cargar_modulos_dinamicos() -> None:
    """Carga dinámicamente los módulos de la carpeta 'modulos'."""
    if registry.MODULOS_DIR.exists():
        for archivo in registry.MODULOS_DIR.glob("*.py"):
            if archivo.name != "__init__.py":
                nombre_modulo = f"chuspacalc.modulos.{archivo.stem}"
                try:
                    importlib.import_module(nombre_modulo)
                except (ImportError, ModuleNotFoundError):
                    pass


def dispatch(subcommand: str) -> int:
    """
    Despacha un subcomando a su función ejecutable correspondiente.

    Args:
        subcommand: Nombre del subcomando a ejecutar.

    Returns:
        Código de salida entero (0 para éxito).

    Examples:
        >>> dispatch("convert")
        Ejecutando conversión...
        0
        >>> dispatch("desconocido")
        Error: subcomando desconocido 'desconocido'
        1
    """
    # Forzamos el descubrimiento automático de submódulos antes de consultar
    _cargar_modulos_dinamicos()

    tools = registry.get_tools()
    handler = tools.get(subcommand)

    if handler is None:
        print(
            f"Error: subcomando desconocido '{subcommand}'",
            file=sys.stderr,
        )
        return 1

    try:
        return handler()
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1
